from dto import *


async def send_message(client_id: int, campaign_id: int):
    print('send message')
    # Логика отправки сообщения, может быть вызов внешнего сервиса
    messages_db.append(Message(id=len(messages_db) + 1, created_at=datetime.now(), status="Sent", campaign_id=campaign_id, client_id=client_id))
    print(f'Пришло сообщение: {messages_db[-1]}')


async def process_campaign(campaign: Campaign):
    print('process campaing')
    # Логика обработки рассылки
    # current_time = datetime.now()
    # if campaign.start_time <= current_time <= campaign.end_time:
    clients_to_notify = [client for client in clients_db if client.tag == campaign.tag_filter]
    for client in clients_to_notify:
        await send_message(client.id, campaign.id)


async def process_active_campaigns():
    print('process_active_campaigns')
    for campaign in campaigns_db:
        await process_campaign(campaign)
