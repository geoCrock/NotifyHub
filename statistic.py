from dto import messages_db, campaigns_db


async def get_campaign_stats(campaign_id: int):
    campaign_messages = [message for message in messages_db if message.campaign_id == campaign_id]
    stats = {"total_messages": len(campaign_messages), "status_counts": {}}
    for message in campaign_messages:
        stats["status_counts"][message.status] = stats["status_counts"].get(message.status, 0) + 1
    return stats


async def get_campaigns_stats():
    stats = {"total_campaigns": len(campaigns_db), "total_messages": len(messages_db), "status_counts": {}}
    for message in messages_db:
        stats["status_counts"][message.status] = stats["status_counts"].get(message.status, 0) + 1
    return stats
