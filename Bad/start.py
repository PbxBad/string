from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

from config import OWNER_ID


# ──────────────────────────────────────
# Command Filter
# ──────────────────────────────────────
def private_cmd(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# ──────────────────────────────────────
# /start Handler
# ──────────────────────────────────────
@Client.on_message(private_cmd("start"))
async def start_handler(bot: Client, msg: Message):
    me = await bot.get_me()

    caption = f"""
✦ » ʜᴇʏ {msg.from_user.mention} ✤,
✦ » ɪ ᴀᴍ {me.mention},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ,
✦ » ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴩʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ
✦ » ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ,
✦ » ᴅᴍ ᴍʏ ᴏᴡɴᴇʀ:
[⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸꯭](tg://user?id={OWNER_ID})
"""

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="⌜ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ⌟",
                    callback_data="generate",
                )
            ],
            [
                InlineKeyboardButton(
                    text="•⌜ ʜᴀᴄᴋ ғᴇᴀᴛᴜʀᴇs ⌟",
                    callback_data="hack_btn",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⌜ sᴜᴘᴘᴏʀᴛ ⌟",
                    url="https://t.me/PBX_CHAT",
                ),
                InlineKeyboardButton(
                    text="⌜ ᴜᴘᴅᴀᴛᴇs ⌟",
                    url="https://t.me/PBX_UPDATE",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⌜ sᴏᴜʀᴄᴇ ⌟",
                    url="https://github.com/PbxBad/string-session-manager/fork",
                )
            ],
        ]
    )

    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/ookphv.jpg",
        caption=caption,
        reply_markup=keyboard,
    )
