from dto import *


async def send_message(client_id: int, newsletter_id: int):
    print('send message')
    # Логика отправки сообщения, может быть вызов внешнего сервиса
    messages_db.append(Message(id=len(messages_db) + 1, created_at=datetime.now(), status="Sent", newsletter_id=newsletter_id, client_id=client_id))
    print(f'Пришло сообщение: {messages_db[-1]}')


async def process_newsletter(newsletter: Newsletter):
    print('process campaing')
    # Логика обработки рассылки
    # current_time = datetime.now()
    # if newsletter.start_time <= current_time <= newsletter.end_time:
    clients_to_notify = [client for client in clients_db if client.tag == newsletter.tag_filter]
    for client in clients_to_notify:
        await send_message(client.id, newsletter.id)


async def process_active_newsletters():
    print('process_active_newsletters')
    for newsletter in newsletters_db:
        await process_newsletter(newsletter)
