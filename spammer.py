from telethon.sync import TelegramClient
from telethon import connection

#my.telegram.org
api_id = 
api_hash = ''

client = TelegramClient('username', api_id, api_hash)
async def main():
    a = input('number of messages (if 0 = infinite) ')
    b = input('text ')
    c = input('target ')
    a1 = int(a)
    if a1 < 0:
        print('the number cannot be less than 0')
        exit()
    i = 0
    if a1 == 0:
        a1 = 1
        while i < a1:           
            await client.send_message(c, b)
    else:
        while i < a1:
            await client.send_message(c, b)
            i = i + 1
    
#    while i < a1:           
#        await client.send_message(c, b)
#
#        i = i + 1
        
with client:
    client.loop.run_until_complete(main())
