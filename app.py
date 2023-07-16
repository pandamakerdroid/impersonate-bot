from telethon.sync import TelegramClient, events
import datetime
import toml
from apscheduler.schedulers.blocking import BlockingScheduler

config = toml.load('config.toml')

with TelegramClient(config['user']['session'], config['user']['api_id'], config['user']['api_hash']) as client:
   client.send_message("me", 'le bot impersonate a démarré')
   #print(client.download_profile_photo('me'))

   def generateGreeting():
      now = datetime.datetime.now()
      greeting = ''
      if (now.hour<18):
         greeting = "Bonjour, mes dames et messieurs! "
      elif(now.hour>=19):
         greeting = "Bonsoir, mes dames et messieurs! "
      return greeting

   @client.on(events.NewMessage(pattern='(?i).*(Hello|自动回复)'))
   async def handler(event):
      await event.reply('Hej! You have reached out to the automated bot answer, please mind that your message will be disregarded nevertheless..')

   @client.on(events.NewMessage(pattern='(?i).*(bot|機器人|机器人)'))
   async def handler(event):
      await event.reply('{}I\'m just a bot, je suis que un Bot🙈'.format(generateGreeting()))

   @client.on(events.NewMessage(pattern='(?i).*(Si|si)'))
   async def handler(event):
      await event.reply('Si o no? Si!')

   @client.on(events.NewMessage(pattern='(?i).*(高富帥|高富帅)'))
   async def handler(event):
      await event.reply('{} 高富帥只是曾經的一個傳說, 而我只是一個機器人唷，夜露死苦！🙈'.format(generateGreeting()))

   #@client.on(events.NewMessage(pattern='(?i).*(阿綱|阿纲)'))
   #async def handler(event):
   #   if(event.chat_id == config['groups']['tom']):
   #      await event.reply('阿綱說要請我們所有人吃帝王蟹, 去台灣得頭等艙往返機票也是阿綱全權負責🙈')

   @client.on(events.NewMessage(pattern='(?i).*(币圈).*(多久了？)'))
   async def handler(event):
      if(event.chat_id == config['groups']['tom']): #Tooms group
         await event.reply('見不得人的緬北無腎俠')

   client.run_until_disconnected()