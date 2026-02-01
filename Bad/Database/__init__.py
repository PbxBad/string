from motor.motor_asyncio import AsyncIOMotorClient
import config

# MongoDB Connection
mongodb = AsyncIOMotorClient(config.MONGO_DB_URI)
db = mongodb.BadStringBot
