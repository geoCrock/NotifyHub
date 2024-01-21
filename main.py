import asyncio
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await process_active_campaigns()
#     yield

app = FastAPI()


class Client(BaseModel):
    id: int
    phone_number: str
    operator_code: str
    tag: str
    timezone: str

class Message(BaseModel):
    id: int
    created_at: datetime
    status: str
    campaign_id: int
    client_id: int

class Campaign(BaseModel):
    id: int
    start_time: datetime
    message_text: str
    client_filter: dict
    end_time: datetime

# Для примера используем простые списки вместо базы данных
clients_db = []
messages_db = []
campaigns_db = []



async def send_message(client_id: int, campaign_id: int):
    print('start3')
    # Логика отправки сообщения, может быть вызов внешнего сервиса
    await asyncio.sleep(1)  # Имитация отправки сообщения
    messages_db.append(Message(id=len(messages_db) + 1, created_at=datetime.now(), status="Sent", campaign_id=campaign_id, client_id=client_id))
    print(f'Пришло сообщение: {messages_db[-1]}')


async def process_campaign(campaign: Campaign):
    print('start2')
    # Логика обработки рассылки
    current_time = datetime.now()
    # if campaign.start_time <= current_time <= campaign.end_time:
    clients_to_notify = [client for client in clients_db if all(client[key] == value for key, value in campaign.client_filter.items())]
    for client in clients_to_notify:
        await send_message(client.id, campaign.id)


async def process_active_campaigns():
    print('start')
    for campaign in campaigns_db:
        await process_campaign(campaign)


@app.post("/clients/")
async def create_client(client: Client):
    clients_db.append(client)
    return {"message": "Client created successfully"}

@app.put("/clients/{client_id}")
async def update_client(client_id: int, updated_client: Client):
    client = next((c for c in clients_db if c.id == client_id), None)
    if client:
        client_dict = client.dict()
        client_dict.update(updated_client.dict())
        return {"message": "Client updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Client not found")

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
    campaign = next((c for c in campaigns_db if c.id == campaign_id), None)
    if campaign:
        campaign_dict = campaign.dict()
        campaign_dict.update(updated_campaign.dict())
        return {"message": "Campaign updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Campaign not found")

@app.delete("/campaigns/{campaign_id}")
async def delete_campaign(campaign_id: int):
    global campaigns_db
    campaigns_db = [c for c in campaigns_db if c.id != campaign_id]
    return {"message": "Campaign deleted successfully"}

@app.get("/campaigns/stats")
async def get_campaigns_stats():
    # Логика для получения общей статистики по рассылкам
    return {"message": "Campaigns stats"}

@app.get("/campaigns/{campaign_id}/stats")
async def get_campaign_stats(campaign_id: int):
    # Логика для получения детальной статистики по конкретной рассылке
    return {"message": f"Campaign {campaign_id} stats"}

# Метод для обработки активных рассылок и отправки сообщений клиентам
def process_active_campaigns2():
    # Логика обработки активных рассылок и отправки сообщений
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
