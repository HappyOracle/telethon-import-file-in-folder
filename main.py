import cmd
from telethon import TelegramClient
from array import array
from telethon import TelegramClient, sync, events
from telethon import TelegramClient, events
import asyncio
#from telethon.tl.functions import
from asyncio import new_event_loop
import collections
import sys
import pyodbc

# НОВАЯ ВЕРСИЯ экспериментальная

api_id = 17876697
api_hash = 'f57224fa791de500d30a17a4fbb650ec'
client = TelegramClient('anon', api_id, api_hash)
chat = -1001299652068 #'me', 5103866250, 1491627223, 418820330, -741750752(test), -1001299652068(it)
client.start()



@client.on(events.NewMessage(chats=(chat)))
async def main(event):
    restart_for_cycle = True
    if chat <= 0:
        file = open(r"C:\Users\Administrator\PycharmProjects\Groupdata.txt", "a+", encoding='utf-16')
        while restart_for_cycle:   #True
            async for message in client.iter_messages(chat):
                from_user = await client.get_entity(message.from_id.user_id)
                print(from_user.username, message.from_id.user_id, message.chat_id, message.id, message.date, message.fwd_from, message.peer_id, message.text)
                msg_text = "{dialog_id} {chat} {id} {date} {fwd_from} {peer_id} {Message}: \n".format(dialog_id=message.from_id.user_id, chat=message.chat_id, id=message.id, date=message.date, fwd_from=message.fwd_from, peer_id=message.peer_id, Message=message.text)
                file.write(msg_text)
            if message.photo or message.file:
                    print('File Name :' + str(message.file.name))
                    path = await client.download_media(message.media) #message.media, "youranypathher"
                    print('File saved to', path)  # printed after download is done
            restart_for_cycle = False
        await asyncio.sleep(99999999999999999999999)
    if chat >= 0:
        file = open(r"C:\Users\Administrator\PycharmProjects\Userdata.txt", "a+", encoding='utf-16')
        while restart_for_cycle:  # True
            async for message in client.iter_messages(chat):
                print(message.chat_id, message.id, message.date, message.fwd_from, message.peer_id, message.text)
                msg_text = "{chat} {id} {date} {fwd_from} {peer_id} {Message}: \n".format(chat=message.chat_id, id=message.id, date=message.date, fwd_from=message.fwd_from, peer_id=message.peer_id, Message=message.text)
                file.write(msg_text)
            if message.photo or message.file:
                print('File Name :' + str(message.file.name))
                path = await client.download_media(message.media)  # message.media, "youranypathher"
                print('File saved to', path)  # printed after download is done
            restart_for_cycle = False
        await asyncio.sleep(99999999999999999999999)


@client.on(events.NewMessage(chats=chat, pattern=rf'\.{cmd}', outgoing=True))
async def handler(event):
    while main(events):
        for output_channel in int(chat):
            await client.forward_messages(output_channel, event.message)
    async for message in client.iter_messages(chat):
        await events.MessageDeleted(print(list.message.id, 'Удаленный сообщение'))

    @client.on(events.MessageDeleted)
    async def handler(event):
        while main(events):
        # Log all deleted message IDs
            for msg_id in event.deleted_ids:
                print('Message', msg_id, 'was deleted in', event.chat_id, event.user_id)
    return   # worked

with client:
    client.loop.run_until_complete(main(events))

#ya ded inside potomu chto ya ded inside no pochemu? potomu chto ya ded inside
