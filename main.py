import asyncio, config, voice

from telethon import TelegramClient, events, functions, types
from gpt import chat_with_gpt
from random import randint

work = [True]
global history
history = {}

api_id = config.api_id
api_hash = config.api_hash
your_id = config.your_id

client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage(chats=your_id))
async def com(event):
	messages = await client.get_messages(event.chat_id)
	user_input = messages[0].text
	if user_input == 'stop':
		work[0] = False
		print('stop')
	elif user_input == 'start':
		work[0] = True
		print('start')

@client.on(events.NewMessage(incoming=True))
async def wait(event):
	if event.chat_id > 0 and work[0]:
		await client.get_dialogs()
		en = await client.get_entity(event.chat_id)
		user = await event.get_sender()
		if not(user.bot):
			print(event.chat_id)
			async with client.action(en, 'game'):
				messages = await client.get_messages(event.chat_id)
				try:
					if messages[0].to_dict()['media']['document']['mime_type'] == 'audio/ogg':
						path = await messages[0].download_media()
						try:
							user_input = voice.voice(config.y_token, config.y_catalog_id, path)
						except ValueError:
							await client.send_message(event.chat_id, "⚠️Ваше голосовое сообщение не должно превышать 1 Мб")
							user_input = ''
				except TypeError:
					user_input = messages[0].text
				except KeyError:
					user_input = messages[0].text
				
				if user_input != '':
					try:
						history[event.chat_id]
					except KeyError:
						history[event.chat_id] = ""
					gpt_response, history[event.chat_id] = chat_with_gpt(user_input, history[event.chat_id], "gpt-3.5-turbo-instruct", api_key=config.gpt_key)
					await asyncio.sleep(3)
					await client.send_message(event.chat_id, gpt_response)
			await asyncio.sleep(20)

async def main():
	await client.start()
	print("Waiting for a message...")
	await client.run_until_disconnected()



client.loop.run_until_complete(main())