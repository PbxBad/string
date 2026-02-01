from Bad.Database import db

# Collections
usersdb = db.tgusersdb
chatsdb = db.tgchatsdb

# ---------------- USERS ---------------- #

async def is_served_user(user_id: int) -> bool:
    return bool(await usersdb.find_one({"user_id": user_id}))


async def get_served_users() -> list:
    return [user async for user in usersdb.find({"user_id": {"$gt": 0}})]


async def add_served_user(user_id: int):
    if await is_served_user(user_id):
        return
    await usersdb.insert_one({"user_id": user_id})


async def remove_served_user(user_id: int):
    await usersdb.delete_one({"user_id": user_id})

# ---------------- CHATS ---------------- #

async def is_served_chat(chat_id: int) -> bool:
    return bool(await chatsdb.find_one({"chat_id": chat_id}))


async def get_served_chats() -> list:
    return [chat async for chat in chatsdb.find({"chat_id": {"$lt": 0}})]


async def add_served_chat(chat_id: int):
    if await is_served_chat(chat_id):
        return
    await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    await chatsdb.delete_one({"chat_id": chat_id})
