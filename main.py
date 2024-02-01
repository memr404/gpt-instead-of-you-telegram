from telethon import TelegramClient, events, functions, types
from gpt import chat_with_gpt
import time, asyncio, config

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
		print(event.chat_id)
		await client.get_dialogs()
		en = await client.get_entity(event.chat_id)
		if not(en.User['bot']):
			async with client.action(en, 'game'):
				messages = await client.get_messages(event.chat_id)
				user_input = messages[0].text
				try:
					history[event.chat_id]
				except KeyError:
					history[event.chat_id] = ""
				gpt_response, history[event.chat_id] = chat_with_gpt(user_input, history[event.chat_id], api_key=config.gpt_key)
				await asyncio.sleep(3)
				await client.send_message(event.chat_id, gpt_response)
			await asyncio.sleep(20)

async def main():
	await client.start()
	print("Waiting for a message...")
	await client.run_until_disconnected()

def stop():
	time.sleep(20)

client.loop.run_until_complete(main())