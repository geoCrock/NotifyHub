import asyncio
import pytz
from dto import *


async def send_message(client_id: int, newsletter_id: int):
    try:
        messages_db.append(Message(id=len(messages_db) + 1, created_at=datetime.now(), status="Sent", newsletter_id=newsletter_id, client_id=client_id))
    except Exception as e:
        print(f"Erorr: {e}")
        return f'Erorr: {e}'

async def process_newsletter(newsletter: Newsletter):
    while datetime.now(pytz.timezone('UTC')) < newsletter.start_time:
        await asyncio.sleep(1)

    if datetime.now(pytz.timezone('UTC')) > newsletter.end_time:
        return {"message": "Time out"}

    clients_to_notify = [client for client in clients_db if client.tag == newsletter.tag_filter]
    for client in clients_to_notify:
        await send_message(client.id, newsletter.id)


async def process_active_newsletters():
    for newsletter in newsletters_db:
        await process_newsletter(newsletter)
