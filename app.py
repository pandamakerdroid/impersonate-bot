import datetime, toml, asyncio, sys
from telethon.sync import TelegramClient, events
from apscheduler.schedulers.asyncio import AsyncIOScheduler

arguments = sys.argv
config = toml.load('config.toml')

sched = AsyncIOScheduler(timezone=arguments[1])
#timezone="Asia/Taipei"
#timezone="Europe/Vienna"
#sched_eu = AsyncIOScheduler(timezone="Europe/Vienna")

def generate_greeting():
    now = datetime.datetime.now()
    greeting = ''
    if now.hour < 18:
        greeting = "Bonjour, mes dames et messieurs! "
    elif now.hour >= 18:
        greeting = "Bonsoir, mes dames et messieurs! "
    return greeting

async def send_message(targets, message):
    if client is not None:
        await client.send_message(targets, message)

async def send_scheduled_greeting(message):
    for target in config['targets']:
        await client.send_message(config['targets'][target], message)

async def send_response(message,event):
    if(event.message._chat_peer.channel_id in config['targets'].values()):
        await event.reply(message)
        
# Event handlers for message events
@events.register(events.NewMessage(pattern='(?i).*(Hello|自动回复)'))
async def handle_hello(event):
    await send_response('Hej! You have reached out to the automated bot answer, please note that your message will be disregarded.', event)

@events.register(events.NewMessage(pattern='(?i).+(gm|早晨|早安)'))
async def handle_good_morning(event):
    await send_response('Bonjour!', event)

@events.register(events.NewMessage(pattern='(?i).+(good evening|晚上好)'))
async def handle_good_evening(event):
    await send_response('Bonsoir!', event)
    
@events.register(events.NewMessage(pattern='(?i).+(gn|晚安|安安)'))
async def handle_good_night(event):
    await send_response('Bonne nuit!', event)
    
@events.register(events.NewMessage(pattern='(?i).*(kfc|肯德基|ＫＦＣ)'))
async def handle_kfc(event):
    greeting = generate_greeting()
    await send_response(f'{greeting}\n這裡尋找你鍾意的套餐唷\nhttps://www.kfcclub.com.tw/menu/hot-meal?mid=40', event)

@events.register(events.NewMessage(pattern='(?i).*(機器人|机器人)'))
async def handle_bot(event):
    greeting = generate_greeting()
    await send_response(f'{greeting}I\'m just a bot, je suis qu\'un Bot🙈', event)

#@sched_eu.scheduled_job('cron', day_of_week='mon', hour=0, minute=30)
@sched.scheduled_job('cron', day_of_week='mon', hour=0, minute=30)
async def sunday_night_greeting():
    await send_scheduled_greeting("Monday 0.30: It's been a full week. As the clock is about to strike midnight, remember to give yourself the rest you need. Sweet dreams, and let's welcome a new week with refreshed energy!")
    await send_scheduled_greeting("星期一,0:30: 經過了滿滿的一周，當鐘即將敲響午夜時，別忘了給自己足夠的休息。甜美的夢境在等你，讓我們以全新的精神迎接新的一周！")
    print('Monday night greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='mon', hour=7, minute=30)
@sched.scheduled_job('cron', day_of_week='mon', hour=7, minute=30)
async def monday_morning_greeting():
    await send_scheduled_greeting("Monday 07.30. Morning! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!")
    await send_scheduled_greeting("星期一, 07:30, 早晨好! 今日新的一周開始，充滿希望的日子。記住，每一天都是一個新的機會，讓我們以積極的態度迎接挑戰吧！")
    print('Monday morning greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='mon', hour=12, minute=00)
@sched.scheduled_job('cron', day_of_week='mon', hour=12, minute=00)
async def monday_noon_greeting():
    await send_scheduled_greeting("Monday 12.00. Halfway through Monday! Keep your spirits high and savor a delightful lunch. Your energy and efforts are making this day fruitful.")
    await send_scheduled_greeting("星期一, 12:00, 星期一已過半！保持高昂的士氣，享用一頓美味的午餐。你的能量和努力正在讓這一天充實。")
    print('Monday noon greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='mon', hour=18, minute=30)
@sched.scheduled_job('cron', day_of_week='mon', hour=18, minute=30)
async def monday_evening_greeting():
    await send_scheduled_greeting("Monday 18.30. Deuce! A great day has come to an end, and your efforts have made the world a better place. Remember, new opportunities are waiting for you tomorrow!")
    await send_scheduled_greeting("星期一, 18:30, 晚上好! 偉大的一天已經結束，你的努力讓這個世界變得更好。記住，明天有新的機會在等待你！")
    print('Monday morning greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='tue', hour=7, minute=30)
@sched.scheduled_job('cron', day_of_week='tue', hour=7, minute=30)
async def tuesday_morning_greeting():
    await send_scheduled_greeting("Tuesday 07.30. Morning! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!")
    await send_scheduled_greeting("星期二, 07:30, 早晨好! 昨日的努力已經過去，新的一天帶來新的可能性。今天就是你繼續奮鬥的日子，加油！")
    print('Tuesday morning greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='tue', hour=12, minute=00)
@sched.scheduled_job('cron', day_of_week='tue', hour=12, minute=00)
async def tuesday_noon_greeting():
    await send_scheduled_greeting("Tuesday 12.00. It's Tuesday noon - take a moment to build your momentum for the week with a nourishing lunch. The best of the day is yet to come.")
    await send_scheduled_greeting("星期二, 12:00, 現在是星期二中午 - 用一頓營養午餐來為這週積蓄動力。一天中最美好的時刻即將來臨。")
    print('Tuesday noon greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='tue', hour=18, minute=30)
@sched.scheduled_job('cron', day_of_week='tue', hour=18, minute=30)
async def tuesday_evening_greeting():
    await send_scheduled_greeting("Tuesday 18.30. Deuces! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!")
    await send_scheduled_greeting("星期二, 18:30, 晚上好! 這一天已經結束，你有所付出，也有所收穫。放下疲慁，為明天充電吧！")
    print('Tuesday evening greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='wed', hour=7, minute=30)
@sched.scheduled_job('cron', day_of_week='wed', hour=7, minute=30)
async def wednesday_morning_greeting():
    await send_scheduled_greeting("Wednesday 07.30. Morning! It's the midpoint of the week, you've already made it halfway through. Keep the spirits up, you're moving towards your goals!")
    await send_scheduled_greeting("星期三, 07:30, 早晨好! 這是一周的中點，你已經走過了一半的路程。繼續保持精神，你正在朝目標前進！")
    print('Wednesday morning greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='wed', hour=12, minute=00)
@sched.scheduled_job('cron', day_of_week='wed', hour=12, minute=00)
async def wednesday_noon_greeting():
    await send_scheduled_greeting("Wednesday 12.00. Congratulations on reaching the midpoint of the week! Celebrate your achievements with a tasty meal. Your hard work is paving your way to success.")
    await send_scheduled_greeting("星期三, 12:00, 恭喜你到達了一週的中點！用一頓美食來慶祝你的成就。你的辛勤工作正在為你鋪平成功的道路。")
    print('Wednesday noon greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='wed', hour=18, minute=30)
@sched.scheduled_job('cron', day_of_week='wed', hour=18, minute=30)
async def wednesday_evening_greeting():
    await send_scheduled_greeting("Wednesday 18.30. Deuces! Your efforts will not be in vain, each day is a step forward. Rest well, prepare for the success of tomorrow.")
    await send_scheduled_greeting("星期三, 18:30, 晚上好! 你的努力不會白費，每一天都是向前的一步。好好休息，為明日的成功做好準備。")
    print('Wednesday evening greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='thu', hour=7, minute=30)
@sched.scheduled_job('cron', day_of_week='thu', hour=7, minute=30)
async def thursday_morning_greeting():
    await send_scheduled_greeting("Thursday 07.30. Morning! A new day, new opportunities. Even if yesterday was challenging, today has the potential to change. Keep smiling, keep pushing!")
    await send_scheduled_greeting("星期四, 07:30, 早晨好! 新的一天，新的機會。即使昨日有困難，今日都有改變的可能。保持微笑，繼續努力！")
    print('Thursday morning greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='thu', hour=12, minute=00)
@sched.scheduled_job('cron', day_of_week='thu', hour=12, minute=00)
async def thursday_noon_greeting():
    await send_scheduled_greeting("Thursday 12.00. It's Thursday noon! You're doing great. Keep up the hard work and reward yourself with a delicious lunch. Replenish your energy for the rest of the day.")
    await send_scheduled_greeting("星期四, 12:00, 現在是星期四中午！你做得很好，繼續努力並用一頓美味的午餐犒賞自己。為今天的剩餘時間補充能量。")
    print('Thursday noon greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='thu', hour=18, minute=30)
@sched.scheduled_job('cron', day_of_week='thu', hour=18, minute=30)
async def thursday_evening_greeting():
    await send_scheduled_greeting("Thursday 18.30. Deuces! One more day to the weekend. You're doing great, keep it up tomorrow!")
    await send_scheduled_greeting("星期四, 18:30, 晚上好! 再過一天，就是週末了。你做得很好，明天繼續加油！")
    print('Thursday evening greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='fri', hour=7, minute=30)
@sched.scheduled_job('cron', day_of_week='fri', hour=7, minute=30)
async def friday_morning_greeting():
    await send_scheduled_greeting("Friday 07.30. Morning! The last day of the workweek, let's embrace this day with utmost enthusiasm! Remember, you have the power to accomplish any goals you set.")
    await send_scheduled_greeting("星期五, 07:30, 早晨好! 最後一個工作日，讓我們以最大的熱情來迎接這一天！不要忘了，你有能力完成任何你設定的目標。")
    print('Friday morning greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='fri', hour=12, minute=00)
@sched.scheduled_job('cron', day_of_week='fri', hour=12, minute=00)
async def friday_noon_greeting():
    await send_scheduled_greeting("Friday 12.00. Friday noon - the weekend is almost here! Stay focused, finish strong, and enjoy a delightful lunch. Every effort is a step towards success.")
    await send_scheduled_greeting("星期五, 12:00, 星期五中午 - 週末快到了！保持專注，堅持到底，並享用一頓美好的午餐。每一份努力都是通往成功的一步。")
    print('Friday noon greeting sent.')

#@sched_eu.scheduled_job('cron', day_of_week='fri', hour=18, minute=30)
@sched.scheduled_job('cron', day_of_week='fri', hour=18, minute=30)
async def friday_evening_greeting():
    await send_scheduled_greeting("Friday 18.30. Deuces! The workweek is over, you did a fantastic job! Relax and enjoy your weekend, you've earned it!")
    await send_scheduled_greeting("星期五, 18:30, 晚上好! 工作一週結束，你做得非常好！放鬆一下，享受你的週末，你值得擁有它!")
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
    global client
    client = TelegramClient(config['user']['session'], config['user']['api_id'], config['user']['api_hash'])
    client.add_event_handler(handle_hello)
    client.add_event_handler(handle_bot)
    client.add_event_handler(handle_kfc)
    client.add_event_handler(handle_good_morning)
    client.add_event_handler(handle_good_evening)
    client.add_event_handler(handle_good_night)
    await client.start()
    await client.run_until_disconnected()

async def main():
    await asyncio.gather(run_client(), run_scheduler())

asyncio.run(main())
