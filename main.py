# import asyncio
import uvicorn
# from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from dto import *
from statistic import get_newsletter_stats, get_newsletters_stats
from send_messages import process_active_newsletters


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await process_active_newsletters()
#     yield

app = FastAPI()


@app.post("/clients/")
async def create_client(client: Client):
    clients_db.append(client)
    return {"message": "Client created successfully"}


@app.put("/clients/{client_id}")
async def update_client(client_id: int, updated_client: Client):
    for client in clients_db:
        if client.id == client_id:
            # Обновляем атрибуты клиента
            client.phone_number = updated_client.phone_number
            client.operator_code = updated_client.operator_code
            client.tag = updated_client.tag
            client.timezone = updated_client.timezone
            return {"message": f"Client with id {client_id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"Client with id {client_id} not found")


@app.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    global clients_db
    clients_db = [c for c in clients_db if c.id != client_id]
    return {"message": "Client deleted successfully"}


@app.post("/newsletters/")
async def create_newsletter(newsletter: Newsletter):
    newsletters_db.append(newsletter)
    await process_active_newsletters()
    return {"message": "Newsletter created successfully"}


@app.put("/newsletters/{newsletter_id}")
async def update_newsletter(newsletter_id: int, updated_newsletter: Newsletter):
    for newsletter in newsletters_db:
        if newsletter.id == newsletter_id:
            # Обновляем атрибуты рассылки
            newsletter.start_time = updated_newsletter.start_time
            newsletter.message_text = updated_newsletter.message_text
            newsletter.tag_filter = updated_newsletter.tag_filter
            newsletter.end_time = updated_newsletter.end_time
            return {"message": f"Newsletter with id {newsletter_id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"Newsletter with id {newsletter_id} not found")


@app.delete("/newsletters/{newsletter_id}")
async def delete_newsletter(newsletter_id: int):
    global newsletters_db
    newsletters_db = [c for c in newsletters_db if c.id != newsletter_id]
    return {"message": "Newsletter deleted successfully"}


@app.get("/newsletters/stats")
async def get_newsletters_stats_endpoint():
    return await get_newsletters_stats()


@app.get("/newsletters/{newsletter_id}/stats")
async def get_newsletter_stats_endpoint(newsletter_id: int):
    return await get_newsletter_stats(newsletter_id)


@app.get("/get_clients/")
async def get_clients():
    return clients_db


@app.get("/get_newsletters/")
async def get_newsletters():
    return newsletters_db


@app.get("/get_messages/")
async def get_messages():
    return messages_db


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
