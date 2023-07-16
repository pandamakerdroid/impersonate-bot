import datetime
import toml
import asyncio
from telethon.sync import TelegramClient, events
from apscheduler.schedulers.asyncio import AsyncIOScheduler

config = toml.load('config.toml')
sched = AsyncIOScheduler(timezone="Asia/Taipei")
client = TelegramClient(config['user']['session'], config['user']['api_id'], config['user']['api_hash'])

def generate_greeting():
    now = datetime.datetime.now()
    greeting = ''
    if now.hour < 18:
        greeting = "Bonjour, mes dames et messieurs! "
    elif now.hour >= 18:
        greeting = "Bonsoir, mes dames et messieurs! "
    return greeting

def send_message(client, grp, message):
    client.send_message(grp, message)

async def send_scheduled_greeting(message):
    for grp in config['groups']:
        await client.send_message(config['groups'][grp], message)

# Event handlers for message events
@events.register(events.NewMessage(pattern='(?i).*(Hello|自动回复)'))
async def handle_hello(event):
    await event.reply('Hej! You have reached out to the automated bot answer, please note that your message will be disregarded.')

@events.register(events.NewMessage(pattern='(?i).*(bot|機器人|机器人)'))
async def handle_bot(event):
    greeting = generate_greeting()
    await event.reply(f'{greeting}I\'m just a bot, je suis qu\'un Bot🙈')

@sched.scheduled_job('cron', day_of_week='sun', hour=23, minute=59)
async def sunday_night_greeting():
    await send_scheduled_greeting("Sunday 23.59: It's been a full week. As the clock is about to strike midnight, remember to give yourself the rest you need. Sweet dreams, and let's welcome a new week with refreshed energy!")
    await send_scheduled_greeting("星期日,23:59: 經過了滿滿的一周，當鐘即將敲響午夜時，別忘了給自己足夠的休息。甜美的夢境在等你，讓我們以全新的精神迎接新的一周！")
    print('Sunday night greeting sent.')

@sched.scheduled_job('cron', day_of_week='mon', hour=7, minute=30)
async def monday_morning_greeting():
    await send_scheduled_greeting("Monday 07.30, Morning! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!")
    await send_scheduled_greeting("星期一, 07:30, 早晨好! 今日新的一周開始，充滿希望的日子。記住，每一天都是一個新的機會，讓我們以積極的態度迎接挑戰吧！")
    print('Monday morning greeting sent.')

@sched.scheduled_job('cron', day_of_week='tue', hour=7, minute=30)
async def tuesday_morning_greeting():
    await send_scheduled_greeting("Tuesday 07.30, Morning! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!")
    await send_scheduled_greeting("星期二, 07:30, 早晨好! 昨日的努力已經過去，新的一天帶來新的可能性。今天就是你繼續奮鬥的日子，加油！")
    print('Tuesday morning greeting sent.')

@sched.scheduled_job('cron', day_of_week='tue', hour=18, minute=30)
async def tuesday_evening_greeting():
    await send_scheduled_greeting("Tuesday 18.00, Deuces! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!")
    await send_scheduled_greeting("星期二, 晚上好! 這一天已經結束，你有所付出，也有所收穫。放下疲慁，為明天充電吧！")
    print('Tuesday evening greeting sent.')

@sched.scheduled_job('cron', day_of_week='wed', hour=7, minute=30)
async def wednesday_morning_greeting():
    await send_scheduled_greeting("Wednesday 07.30, Morning! It's the midpoint of the week, you've already made it halfway through. Keep the spirits up, you're moving towards your goals!")
    await send_scheduled_greeting("星期三, 07:30, 早晨好! 這是一周的中點，你已經走過了一半的路程。繼續保持精神，你正在朝目標前進！")
    print('Wednesday morning greeting sent.')

@sched.scheduled_job('cron', day_of_week='wed', hour=18, minute=30)
async def wednesday_evening_greeting():
    await send_scheduled_greeting("Wednesday 18.00, Deuces! Your efforts will not be in vain, each day is a step forward. Rest well, prepare for the success of tomorrow.")
    await send_scheduled_greeting("星期三, 晚上好! 你的努力不會白費，每一天都是向前的一步。好好休息，為明日的成功做好準備。")
    print('Wednesday evening greeting sent.')

@sched.scheduled_job('cron', day_of_week='thu', hour=7, minute=30)
async def thursday_morning_greeting():
    await send_scheduled_greeting("Thursday 07.30, Morning! A new day, new opportunities. Even if yesterday was challenging, today has the potential to change. Keep smiling, keep pushing!")
    await send_scheduled_greeting("星期四, 07:30, 早晨好! 新的一天，新的機會。即使昨日有困難，今日都有改變的可能。保持微笑，繼續努力！")
    print('Thursday morning greeting sent.')

@sched.scheduled_job('cron', day_of_week='thu', hour=18, minute=30)
async def thursday_evening_greeting():
    await send_scheduled_greeting("Thursday 18.00, Deuces! One more day to the weekend. You're doing great, keep it up tomorrow!")
    await send_scheduled_greeting("星期四, 晚上好! 再過一天，就是週末了。你做得很好，明天繼續加油！")
    print('Thursday evening greeting sent.')

@sched.scheduled_job('cron', day_of_week='fri', hour=7, minute=30)
async def friday_morning_greeting():
    await send_scheduled_greeting("Friday 07.30, Morning! The last day of the workweek, let's embrace this day with utmost enthusiasm! Remember, you have the power to accomplish any goals you set.")
    await send_scheduled_greeting("星期五, 07:30, 早晨好! 最後一個工作日，讓我們以最大的熱情來迎接這一天！不要忘了，你有能力完成任何你設定的目標。")
    print('Friday morning greeting sent.')

@sched.scheduled_job('cron', day_of_week='fri', hour=18, minute=30)
async def friday_evening_greeting():
    await send_scheduled_greeting("Friday 18.00, Deuces! The workweek is over, you did a fantastic job! Relax and enjoy your weekend, you've earned it!")
    await send_scheduled_greeting("星期五, 晚上好! 工作一週結束，你做得非常好！放鬆一下，享受你的週末，你值得擁有它!")
    print('Friday evening greeting sent.')

#@sched.scheduled_job('interval', seconds=2)
#async def timed_job():
#    await send_scheduled_greeting("Test message, sorry for spamming.")
#    await send_scheduled_greeting("測試用訊息, 抱歉灌水了,1l4fu04h96ej94:D")
#    print('This job is run every 2 seconds.')

async def run_scheduler():
    sched.start()
    while True:
        await asyncio.sleep(1)

async def run_client():
    client.add_event_handler(handle_hello)
    client.add_event_handler(handle_bot)
    await client.start()
    await client.run_until_disconnected()

async def main():
    await asyncio.gather(run_client(), run_scheduler())

asyncio.run(main())
