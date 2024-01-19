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

# Аналогично реализовать методы для рассылок и сообщений

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
