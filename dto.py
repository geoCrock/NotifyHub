from pydantic import BaseModel
from datetime import datetime


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
    tag_filter: str
    end_time: datetime


# Для примера используем простые списки вместо базы данных
clients_db = []
messages_db = []
campaigns_db = []
