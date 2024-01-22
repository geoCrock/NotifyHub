# import asyncio
import uvicorn
# from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from dto import *
from statistic import get_campaign_stats, get_campaigns_stats
from send_messages import process_active_campaigns

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await process_active_campaigns()
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


@app.post("/campaigns/")
async def create_campaign(campaign: Campaign):
    campaigns_db.append(campaign)
    await process_active_campaigns()
    return {"message": "Campaign created successfully"}


@app.put("/campaigns/{campaign_id}")
async def update_campaign(campaign_id: int, updated_campaign: Campaign):
    for campaign in campaigns_db:
        if campaign.id == campaign_id:
            # Обновляем атрибуты рассылки
            campaign.start_time = updated_campaign.start_time
            campaign.message_text = updated_campaign.message_text
            campaign.client_filter = updated_campaign.client_filter
            campaign.end_time = updated_campaign.end_time
            return {"message": f"Campaign with id {campaign_id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"Campaign with id {campaign_id} not found")


@app.delete("/campaigns/{campaign_id}")
async def delete_campaign(campaign_id: int):
    global campaigns_db
    campaigns_db = [c for c in campaigns_db if c.id != campaign_id]
    return {"message": "Campaign deleted successfully"}


@app.get("/campaigns/stats")
async def get_campaigns_stats_endpoint():
    return await get_campaigns_stats()


@app.get("/campaigns/{campaign_id}/stats")
async def get_campaign_stats_endpoint(campaign_id: int):
    return await get_campaign_stats(campaign_id)


@app.get("/get_clients/")
async def get_clients():
    return clients_db


@app.get("/get_camp/")
async def get_camp():
    return campaigns_db


@app.get("/get_messages/")
async def get_messages():
    return messages_db


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
