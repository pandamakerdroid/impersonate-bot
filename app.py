import toml, asyncio, sys
from telethon.sync import TelegramClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from jobs.regex_reactions import (
    handle_bot,
    handle_good_morning,
    handle_good_evening,
    handle_good_night,
    handle_hello,
    handle_kfc,
    handle_ramen
)
from jobs.daily_greetings import (
    sunday_night_greeting,
    monday_morning_greeting,
    monday_noon_greeting,
    monday_evening_greeting,
    tuesday_morning_greeting,
    tuesday_noon_greeting,
    tuesday_evening_greeting,
    wednesday_morning_greeting,
    wednesday_noon_greeting,
    wednesday_evening_greeting,
    thursday_morning_greeting,
    thursday_noon_greeting,
    thursday_evening_greeting,
    friday_morning_greeting,
    friday_evening_greeting,
    friday_noon_greeting,
    test_job
)

arguments = sys.argv
config = toml.load('config.toml')

sched = AsyncIOScheduler(timezone="Asia/Taipei")
sched_vie = AsyncIOScheduler(timezone="Europe/Vienna")

def setup_scheduler(sched, targets):
    #sched.add_job(test_job,'interval', [client, targets], seconds = 2)
    sched.add_job(sunday_night_greeting,'cron', [client, targets], day_of_week='mon', hour=0, minute=30 )
    sched.add_job(monday_morning_greeting,'cron', [client, targets], day_of_week='mon', hour=7, minute=30 )
    sched.add_job(monday_noon_greeting,'cron', [client, targets], day_of_week='mon', hour=12, minute=30 )
    sched.add_job(monday_evening_greeting,'cron', [client, targets], day_of_week='mon', hour=18, minute=30 )
    sched.add_job(tuesday_morning_greeting,'cron', [client, targets], day_of_week='tue', hour=7, minute=30 )
    sched.add_job(tuesday_noon_greeting,'cron', [client, targets], day_of_week='tue', hour=12, minute=00 )
    sched.add_job(tuesday_evening_greeting,'cron', [client, targets], day_of_week='tue', hour=18, minute=30 )
    sched.add_job(wednesday_morning_greeting,'cron', [client, targets], day_of_week='wed', hour=7, minute=30 )
    sched.add_job(wednesday_noon_greeting,'cron', [client, targets], day_of_week='wed', hour=12, minute=00 )
    sched.add_job(wednesday_evening_greeting,'cron', [client, targets], day_of_week='wed', hour=18, minute=30 )
    sched.add_job(thursday_morning_greeting,'cron', [client, targets], day_of_week='thu', hour=7, minute=30 )
    sched.add_job(thursday_noon_greeting,'cron', [client, targets], day_of_week='thu', hour=12, minute=00 )
    sched.add_job(thursday_evening_greeting,'cron', [client, targets], day_of_week='thu', hour=18, minute=30 )
    sched.add_job(friday_morning_greeting,'cron', [client, targets], day_of_week='fri', hour=7, minute=30 )
    sched.add_job(friday_noon_greeting,'cron', [client, targets], day_of_week='fri', hour=12, minute=00 )
    sched.add_job(friday_evening_greeting,'cron', [client, targets], day_of_week='fri', hour=18, minute=30 )
    sched.start()
async def run_scheduler():
    setup_scheduler(sched=sched,targets=config['targets'])
    setup_scheduler(sched=sched_vie,targets=config['targets_vie'])
    while True:
        await asyncio.sleep(1)

async def run_client():
    global client
    client = TelegramClient(config['user']['session'], config['user']['api_id'], config['user']['api_hash'])
    client.add_event_handler(handle_hello)
    client.add_event_handler(handle_bot)
    client.add_event_handler(handle_kfc)
    client.add_event_handler(handle_ramen)
    client.add_event_handler(handle_good_morning)
    client.add_event_handler(handle_good_evening)
    client.add_event_handler(handle_good_night)
    await client.start()
    await client.run_until_disconnected()

async def main():
    await asyncio.gather(run_client())
    await asyncio.gather(run_scheduler())

asyncio.run(main())
