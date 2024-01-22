from dto import messages_db, newsletters_db


async def get_newsletter_stats(newsletter_id: int):
    newsletter_messages = [message for message in messages_db if message.newsletter_id == newsletter_id]
    stats = {"total_messages": len(newsletter_messages), "status_counts": {}}
    for message in newsletter_messages:
        stats["status_counts"][message.status] = stats["status_counts"].get(message.status, 0) + 1
    return stats


async def get_newsletters_stats():
    stats = {"total_newsletters": len(newsletters_db), "total_messages": len(messages_db), "status_counts": {}}
    for message in messages_db:
        stats["status_counts"][message.status] = stats["status_counts"].get(message.status, 0) + 1
    return stats
