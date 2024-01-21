import uvicorn
from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import List

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

@app.post("/campaigns/")
async def create_campaign(campaign: Campaign):
    campaigns_db.append(campaign)
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

@app.post("/messages/")
async def create_message(message: Message):
    messages_db.append(message)
    return {"message": "Message created successfully"}

@app.get("/messages/{campaign_id}")
async def get_messages_for_campaign(campaign_id: int):
    campaign_messages = [m.dict() for m in messages_db if m.campaign_id == campaign_id]
    if not campaign_messages:
        raise HTTPException(status_code=404, detail="No messages found for the campaign")
    return campaign_messages

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
