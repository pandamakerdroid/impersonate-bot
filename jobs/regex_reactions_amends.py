from telethon.sync import events
from utils.generate_greeting import generate_greeting
import toml

config = toml.load('config.toml')
global is_second_active
is_second_active = False

def Merge(dict_1, dict_2 = None, dict_3 = None):
    if (dict_2 is not None):
        dict_1.update(dict_2)
    if (dict_3 is not None):
        dict_1.update(dict_3)
    return dict_1

async def send_response(message,event,targets=Merge(config['targets_amends'])):
    try:
       print(f'keywords triggered by: {str(event.message._chat_peer.channel_id)}')
       if(event.message._chat_peer.channel_id in targets.values()):
           await event.reply(message)
    except AttributeError:
       print(f'keywords triggered by: {str(event.message._chat_peer.user_id)}')
       if(event.message._chat_peer.user_id in targets.values()):
           await event.reply(message)



# Event handlers for message events
@events.register(events.NewMessage(pattern='(?i).*(你欺负人|你討厭|你讨厌)'))
async def handle_first_response(event):
    determine_second_sequence(True)
    await send_response('我爱你。都是我的错。我来哄你。你想干什么我都答应。', event)

@events.register(events.NewMessage(pattern='(?i)^(?!.*(你欺负人|你討厭|你讨厌)).*$'))
async def handle_second_response(event):
    if(determine_second_sequence(None)):
        determine_second_sequence(False)
        await send_response(f'好的，就按你说得来. 为了你开心，干什么都行。🙈', event)

def determine_second_sequence(active=None):
    global is_second_active
    if(active is not None):
        is_second_active = active
        return is_second_active
    elif (active is None and is_second_active is not None):
        return is_second_active
    return False