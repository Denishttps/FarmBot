from pyrogram import Client, filters, types
import logging, config, datetime, run
import os

api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
logging.basicConfig(level=logging.INFO)

app = Client(__name__, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(chats=config.chat_id) & filters.user(users=config.chat_id))
async def farm(bot: Client, msg: types.Message):
    if msg.text.startswith("✅ ЗАЧЁТ!"):
        schedule_date = datetime.datetime.now() + datetime.timedelta(minutes=2)
        await bot.send_message(chat_id=config.chat_id, text="!ферма", schedule_date=schedule_date)
    else:
        time = msg.text.rsplit(maxsplit=6)[1:]
        schedule = datetime.datetime.now() + datetime.timedelta(hours=int(time[0]), minutes=int(time[2])+1)
        await bot.send_message(chat_id=config.chat_id, text="!ферма", schedule_date=schedule)



if __name__ == "__main__":
    run.keep_alive()
    app.run()