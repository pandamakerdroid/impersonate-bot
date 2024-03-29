from telethon.sync import events
from utils.generate_greeting import generate_greeting
import toml

config = toml.load('config.toml')

def Merge(dict_1, dict_2 = None, dict_3 = None):
    if (dict_2 is not None):
        dict_1.update(dict_2)
    if (dict_3 is not None):
        dict_1.update(dict_3)
    return dict_1

async def send_response(message,event,targets=Merge(config['targets'],config['targets_vie'])):
    try:
       print(f'keywords triggered by: {str(event.message._chat_peer.channel_id)}')
       if(event.message._chat_peer.channel_id in targets.values()):
           await event.reply(message)
    except AttributeError:
       print(f'keywords triggered by: {str(event.message._chat_peer.user_id)}')
       if(event.message._chat_peer.user_id in targets.values()):
           await event.reply(message)

# Event handlers for message events
@events.register(events.NewMessage(pattern='(?i).*(Hello|自动回复)'))
async def handle_hello(event):
    await send_response('Hej! You have reached out to the automated bot answer, please note that your message will be disregarded.', event)

#ned mein bevorzugter Ansatz, aber telethon unterstützte keine extra Parameter
@events.register(events.NewMessage(pattern='(?i).*(ramen|拉面|拉麵)'))
async def handle_ramen(event):
    await send_response('Hast du Heute lust auf Takumi oder Shoyu, meine Liebe?', event, targets=config['targets_vie'])

@events.register(events.NewMessage(pattern='(?i).*(gm|早晨|早安|morning|bonjour|morgen|moin|boungiorno|bom dia|buenos dias)'))
async def handle_good_morning(event):
    await send_response('Bonjour!', event)

@events.register(events.NewMessage(pattern='(?i).*(good evening|晚上好|bonsoir|bonasera)'))
async def handle_good_evening(event):
    await send_response('Bonsoir!', event)
    
@events.register(events.NewMessage(pattern='(?i).*(gn|晚安|安安|good night|bonne nuit)'))
async def handle_good_night(event):
    await send_response('Bonne nuit!', event)
    
@events.register(events.NewMessage(pattern='(?i).*(kfc|肯德基|ＫＦＣ)'))
async def handle_kfc(event):
    greeting = generate_greeting()
    await send_response(f'{greeting}\n這裡尋找你鍾意的套餐唷\nKFC 肯德基 臺灣: https://tinyurl.com/2de39hzw\nKFC 肯德基 香港: https://tinyurl.com/2g6wp8b8', event, targets=Merge(config['targets'],config['targets_vie'], config['targets_kfc']))

@events.register(events.NewMessage(pattern='(?i).*(機器人|机器人)'))
async def handle_bot(event):
    greeting = generate_greeting()
    await send_response(f'{greeting}I\'m just a bot, je suis qu\'un Bot🙈', event)
