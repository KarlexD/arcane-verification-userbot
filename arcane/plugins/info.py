from pyrogram import filters
from .. import bot, ARCANEUSER
from pyrogram.types import Message


@bot.on_message(filters.command("info", ['/', ".", "?"]))
async def kk(_, m: Message):
    user = m.from_user.id
    if user in ARCANEUSER:
        await m.reply_text(
            f"**You Are [{m.from_user.first_name}](tg://user?id={user}) Arcane Member**"
        )
