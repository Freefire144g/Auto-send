from telethon import TelegramClient, events
import time

api_id = 13121914
api_hash = '3cfad22d7262c48ee29e734a47934399'
client = TelegramClient('auto_reply_bot', api_id, api_hash)

replied_users = set()

@client.on(events.NewMessage)
async def handle_message(event):
    try:
        if event.is_private and event.sender_id not in replied_users:
            await event.respond("اهلا وسهلا عزيزي سجاد غير متوفر الان وانا الرد التلقائي 👾🤖")
            replied_users.add(event.sender_id)
            print(f"تم الرد على هذا الشخص برد تلقائي : {event.sender_id}")
            time.sleep(2)

    except Exception as e:
        print(f"خطأ: {str(e)}")

print("اشتغلت...")
client.start()
client.run_until_disconnected()