
# Louis Philippe B. Facun
# DogeClick Bot Channel from dogeclick.com
# Auto joiner (/join)

import asyncio
import logging
import re
import time
import os
import sys

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

''' DogeClick Bot Channel from dogeclick.com
Options:
1. Dogecoin_click_bot
2. Litecoin_click_bot
3. BCH_click_bot
4. Zcash_click_bot
5. Bitcoinclick_bot
# '''
dogeclick_channel = 'Dogecoin_click_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print(Fore.MAGENTA + '__      _____ _    ___ ___  __  __ ___ ')
	print(Fore.MAGENTA + '\ \    / / __| |  / __/ _ \|  \/  | __|')
	print(Fore.MAGENTA + ' \ \/\/ /| _|| |_| (_| (_) | |\/| | _| ')
	print(Fore.MAGENTA + '  \_/\_/ |___|____\___\___/|_|  |_|___|\n' + Fore.RESET)
	print(Fore.GREEN + '    -   BY LOUIS PHILIPPE FACUN   -   \n' + Fore.RESET)
                                
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	print(f'Current account: {me.first_name}({me.username})\n')
	print_msg_time('Sending /bots command')
	
	# Start command /bots
	await client.send_message(dogeclick_channel, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{channel_name}...')
			await client.send_message(channel_name, '/start')
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=channel_name, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(dogeclick_channel, msg_id, channel_name)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
	# No more ads
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
			e = input('Press any key to exit...')
			exit(1)
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
