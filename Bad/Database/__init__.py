from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
import sys

try:
    mongodb = AsyncIOMotorClient(MONGO_DB_URI)
    db = mongodb.PurviStringBot
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    print("Please check your MongoDB URL in config.py")
    sys.exit(1)
