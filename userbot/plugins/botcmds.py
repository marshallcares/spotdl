from telethon import events
from telethon import Button
from datetime import datetime
from userbot import catub
from ..Config import Config

botusername = Config.TG_BOT_USERNAME
users = Config.OWNER_ID

@catub.bot_cmd(
    pattern=f"^/ping({botusername})?([\s]+)?$",
    from_users=users,
)
async def ping(event):
    start = datetime.now()
    b=Button.inline('Stats', data='stats')
    catevent = await tgbot.send_message(event.chat_id, "π£πΌπ»π΄", buttons=b, reply_to=event.id)
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await catevent.edit(f"π£πΌπ»π΄\n`{ms}` ππ")


@catub.bot_cmd(
    pattern=f"^/menu({botusername})?([\s]+)?$",
    from_users=users,
)
async def helpmenu(event):
    b=Button.inline('Click', data='mainmenu')
    m = await tgbot.send_message(event.chat_id, "**Open Help Menu**", buttons=b, reply_to=event.id)
