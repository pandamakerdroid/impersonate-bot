
async def send_message(client, targets, message):
    if client is not None:
        await client.send_message(targets, message)

async def send_scheduled_greeting(message, client, targets):
    for target in targets:
        await send_message(client, target, message)

async def sunday_night_greeting(client, targets):
    await send_scheduled_greeting("Sunday 23.30: It's been a full week. As the clock is about to strike midnight, remember to give yourself the rest you need. Sweet dreams, and let's welcome a new week with refreshed energy! Good night!", client, targets)
    await send_scheduled_greeting("星期日, 23:30: 經過了滿滿的一周，當鐘即將敲響午夜時，別忘了給自己足夠的休息。甜美的夢境在等你，讓我們以全新的精神迎接新的一周！好夢！", client, targets)
    print('Sunday night greeting sent.')

async def monday_morning_greeting(client, targets):
    await send_scheduled_greeting("Monday 07.30. Morning! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!", client, targets)
    await send_scheduled_greeting("星期一, 07:30, 早晨好! 今日新的一周開始，充滿希望的日子。記住，每一天都是一個新的機會，讓我們以積極的態度迎接挑戰吧！", client, targets)
    print('Monday morning greeting sent.')

async def monday_noon_greeting(client, targets):
    await send_scheduled_greeting("Monday 12.00. Halfway through Monday! Keep your spirits high and savor a delightful lunch. Your energy and efforts are making this day fruitful.", client, targets)
    await send_scheduled_greeting("星期一, 12:00, 星期一已過半！保持高昂的士氣，享用一頓美味的午餐。你的能量和努力正在讓這一天充實。", client, targets)
    print('Monday noon greeting sent.')

async def monday_evening_greeting(client, targets):
    await send_scheduled_greeting("Monday 18.30. Deuce! A great day has come to an end, and your efforts have made the world a better place. Remember, new opportunities are waiting for you tomorrow!", client, targets)
    await send_scheduled_greeting("星期一, 18:30, 晚上好! 偉大的一天已經結束，你的努力讓這個世界變得更好。記住，明天有新的機會在等待你！", client, targets)
    print('Monday morning greeting sent.')

async def monday_night_greeting(client, targets):
    await send_scheduled_greeting("Monday 23.30. It's Monday night - you've kickstarted the week with resilience. Now, take a deep breath and relax. A restful sleep tonight will fuel a productive tomorrow. Good night!", client, targets)
    await send_scheduled_greeting("星期一, 23:30, 這是星期一的夜晚 - 你以韌性開始了這週。現在，深吸一口氣並放鬆。今晚的充足睡眠將為明天的效率注入能量。好夢！", client, targets)
    print('Monday night greeting sent.')

async def tuesday_morning_greeting(client, targets):
    await send_scheduled_greeting("Tuesday 07.30. Morning! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!", client, targets)
    await send_scheduled_greeting("星期二, 07:30, 早晨好! 昨日的努力已經過去，新的一天帶來新的可能性。今天就是你繼續奮鬥的日子，加油！", client, targets)
    print('Tuesday morning greeting sent.')

async def tuesday_noon_greeting(client, targets):
    await send_scheduled_greeting("Tuesday 12.00. It's Tuesday noon - take a moment to build your momentum for the week with a nourishing lunch. The best of the day is yet to come.", client, targets)
    await send_scheduled_greeting("星期二, 12:00, 現在是星期二中午 - 用一頓營養午餐來為這週積蓄動力。一天中最美好的時刻即將來臨。", client, targets)
    print('Tuesday noon greeting sent.')

async def tuesday_evening_greeting(client, targets):
    await send_scheduled_greeting("Tuesday 18.30. Deuces! Today marks the start of a new week, a day full of hope. Remember, every day is a new opportunity. Let's tackle the challenges with a positive attitude!", client, targets)
    await send_scheduled_greeting("星期二, 18:30, 晚上好! 這一天已經結束，你有所付出，也有所收穫。放下疲慁，為明天充電吧！", client, targets)
    print('Tuesday evening greeting sent.')

async def tuesday_night_greeting(client, targets):
    await send_scheduled_greeting("Tuesday 23.30. As Tuesday comes to a close, remember that rest is just as important as work. Take the time to unwind and prepare for the opportunities that Wednesday will bring. Good night!", client, targets)
    await send_scheduled_greeting("星期二, 23:30, 星期二即將結束，請記住休息與工作同樣重要。花時間放鬆，為星期三將帶來的機會做好準備。好夢！", client, targets)
    print('Tuesday night greeting sent.')

async def wednesday_morning_greeting(client, targets):
    await send_scheduled_greeting("Wednesday 07.30. Morning! It's the midpoint of the week, you've already made it halfway through. Keep the spirits up, you're moving towards your goals!", client, targets)
    await send_scheduled_greeting("星期三, 07:30, 早晨好! 這是一周的中點，你已經走過了一半的路程。繼續保持精神，你正在朝目標前進！", client, targets)
    print('Wednesday morning greeting sent.')

async def wednesday_noon_greeting(client, targets):
    await send_scheduled_greeting("Wednesday 12.00. Congratulations on reaching the midpoint of the week! Celebrate your achievements with a tasty meal. Your hard work is paving your way to success.", client, targets)
    await send_scheduled_greeting("星期三, 12:00, 恭喜你到達了一週的中點！用一頓美食來慶祝你的成就。你的辛勤工作正在為你鋪平成功的道路。", client, targets)
    print('Wednesday noon greeting sent.')

async def wednesday_evening_greeting(client, targets):
    await send_scheduled_greeting("Wednesday 18.30. Deuces! Your efforts will not be in vain, each day is a step forward. Rest well, prepare for the success of tomorrow.", client, targets)
    await send_scheduled_greeting("星期三, 18:30, 晚上好! 你的努力不會白費，每一天都是向前的一步。好好休息，為明日的成功做好準備。", client, targets)
    print('Wednesday evening greeting sent.')

async def wednesday_night_greeting(client, targets):
    await send_scheduled_greeting("Wednesday 23.30. You've made it to the middle of the week! Unwind from the challenges of the day and recharge your energy. Tomorrow is another day to make your mark. Good night!", client, targets)
    await send_scheduled_greeting("星期三, 23:30, 你已經到達了一週的中點！放鬆今天的挑戰，並充電。明天又是一個留下印記的日子。好夢！", client, targets)
    print('Wednesday night greeting sent.')

async def thursday_morning_greeting(client, targets):
    await send_scheduled_greeting("Thursday 07.30. Morning! A new day, new opportunities. Even if yesterday was challenging, today has the potential to change. Keep smiling, keep pushing!", client, targets)
    await send_scheduled_greeting("星期四, 07:30, 早晨好! 新的一天，新的機會。即使昨日有困難，今日都有改變的可能。保持微笑，繼續努力！", client, targets)
    print('Thursday morning greeting sent.')

async def thursday_noon_greeting(client, targets):
    await send_scheduled_greeting("Thursday 12.00. It's Thursday noon! You're doing great. Keep up the hard work and reward yourself with a delicious lunch. Replenish your energy for the rest of the day.", client, targets)
    await send_scheduled_greeting("星期四, 12:00, 現在是星期四中午！你做得很好，繼續努力並用一頓美味的午餐犒賞自己。為今天的剩餘時間補充能量。", client, targets)
    print('Thursday noon greeting sent.')

async def thursday_evening_greeting(client, targets):
    await send_scheduled_greeting("Thursday 18.30. Deuces! One more day to the weekend. You're doing great, keep it up tomorrow!", client, targets)
    await send_scheduled_greeting("星期四, 18:30, 晚上好! 再過一天，就是週末了。你做得很好，明天繼續加油！", client, targets)
    print('Thursday evening greeting sent.')

async def thursday_night_greeting(client, targets):
    await send_scheduled_greeting("Thursday 23.30. Thursday is drawing to a close. As you rest tonight, remember that every sunrise offers a fresh start. Prepare for an energetic Friday. Good night!", client, targets)
    await send_scheduled_greeting("星期四, 23:30, 星期四即將結束。當你今晚休息時，請記住每一個日出都提供了一個新的開始。為充滿活力的星期五做好準備。好夢！", client, targets)
    print('Thursday night greeting sent.')

async def friday_morning_greeting(client, targets):
    await send_scheduled_greeting("Friday 07.30. Morning! The last day of the workweek, let's embrace this day with utmost enthusiasm! Remember, you have the power to accomplish any goals you set.", client, targets)
    await send_scheduled_greeting("星期五, 07:30, 早晨好! 最後一個工作日，讓我們以最大的熱情來迎接這一天！不要忘了，你有能力完成任何你設定的目標。", client, targets)
    print('Friday morning greeting sent.')

async def friday_noon_greeting(client, targets):
    await send_scheduled_greeting("Friday 12.00. Friday noon - the weekend is almost here! Stay focused, finish strong, and enjoy a delightful lunch. Every effort is a step towards success.", client, targets)
    await send_scheduled_greeting("星期五, 12:00, 星期五中午 - 週末快到了！保持專注，堅持到底，並享用一頓美好的午餐。每一份努力都是通往成功的一步。", client, targets)
    print('Friday noon greeting sent.')

async def friday_evening_greeting(client, targets):
    await send_scheduled_greeting("Friday 18.30. Deuces! The workweek is over, you did a fantastic job! Relax and enjoy your weekend, you've earned it!", client, targets)
    await send_scheduled_greeting("星期五, 18:30, 晚上好! 工作一週結束，你做得非常好！放鬆一下，享受你的週末，你值得擁有它!", client, targets)
    print('Friday evening greeting sent.')

async def friday_night_greeting(client, targets):
    await send_scheduled_greeting("Friday 23.30. Friday night is here! After a hardworking week, it's time to rest and rejuvenate. Sleep well tonight and wake up refreshed for a joyful weekend. Good night!", client, targets)
    await send_scheduled_greeting("星期五, 23:30, 星期五的夜晚來臨了！經過一週的辛勤工作，現在是時候休息和恢復活力。今晚好好睡覺，醒來後會對周末充滿喜悅。好夢！", client, targets)
    print('Friday night greeting sent.')

async def test_job(client, targets):
    await send_scheduled_greeting("Test message, sorry for spamming.", client, targets)
    await send_scheduled_greeting("測試用訊息, 抱歉灌水了,1l4fu04h96ej94:D", client, targets)
    print('This job is run every 2 seconds.')