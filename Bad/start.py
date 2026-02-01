from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

from config import OWNER_ID, LOGGER_ID
from Bad.Database.users import add_served_user, is_served_user

# ══════════════════════════════════════
# Command Filter
# ══════════════════════════════════════

def private_cmd(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

# ══════════════════════════════════════
# /start Handler  
# ══════════════════════════════════════

@Client.on_message(private_cmd("start"))
async def start_handler(bot: Client, msg: Message):
    # Check if user is new
    is_new_user = not await is_served_user(msg.from_user.id)
    
    # Add user to database
    await add_served_user(msg.from_user.id)
    
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
⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸꯭
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
                    text="⌜ ʜᴀᴄᴋ ғᴇᴀᴛᴜʀᴇs ⌟",
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
        has_spoiler=True,
        caption=caption,
        reply_markup=keyboard,
    )
    
    # ══════════════════════════════════════
    # SEND NOTIFICATION TO LOGGER GROUP
    # ══════════════════════════════════════
    try:
        user = msg.from_user
        user_mention = user.mention
        user_id = user.id
        username = f"@{user.username}" if user.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        
        # Create user status text
        if is_new_user:
            status = "🆕 **ɴᴇᴡ ᴜsᴇʀ**"
        else:
            status = "🔄 **ʀᴇᴛᴜʀɴɪɴɢ ᴜsᴇʀ**"
        
        # Get total users count
        from Bad.Database.users import get_served_users_count
        total_users = await get_served_users_count()
        
        # Create logger message
        logger_text = f"""
{status}

**👤 ᴜsᴇʀ ɪɴғᴏ:**
├ **ɴᴀᴍᴇ:** {user_mention}
├ **ᴜsᴇʀɴᴀᴍᴇ:** {username}
├ **ᴜsᴇʀ ɪᴅ:** `{user_id}`
└ **ᴀᴄᴛɪᴏɴ:** sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ

**📊 ᴛᴏᴛᴀʟ ᴜsᴇʀs:** {total_users}
"""
        
        # Create inline button for user profile
        logger_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="👤 ᴠɪᴇᴡ ᴜsᴇʀ",
                        url=f"tg://user?id={user_id}"
                    )
                ]
            ]
        )
        
        # Default fallback image
        default_image = "https://files.catbox.moe/ookphv.jpg"
        
        # Try to get user profile photo
        try:
            photos = await bot.get_profile_photos(user_id, limit=1)
            if photos.total_count > 0:
                # Send with user's profile photo
                await bot.send_photo(
                    chat_id=LOGGER_ID,
                    photo=photos.photos[0].file_id,
                    caption=logger_text,
                    reply_markup=logger_keyboard
                )
            else:
                # Send with default image if no profile picture
                await bot.send_photo(
                    chat_id=LOGGER_ID,
                    photo=default_image,
                    caption=logger_text,
                    reply_markup=logger_keyboard
                )
        except Exception as e:
            # Fallback to default image if photo fetch fails
            try:
                await bot.send_photo(
                    chat_id=LOGGER_ID,
                    photo=default_image,
                    caption=logger_text,
                    reply_markup=logger_keyboard
                )
            except:
                # Ultimate fallback to text message
                await bot.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    reply_markup=logger_keyboard
                )
        
    except Exception as e:
        print(f"Failed to send logger notification: {e}")
