from pyrogram import filters
from .. import bot, ARCANEUSER
from pyrogram.types import Message


@bot.on_message(filters.new_chat_members)
async def arcane(_, m: Message):
    user = m.from_user.id
    if user in ARCANEUSER:
        await m.reply_text(
            f"**Welcome The Union [{m.from_user.first_name}-Kun](tg://user?id={user}) Member                        
            Member Number {count}**" 
        )
    else:
        pass
