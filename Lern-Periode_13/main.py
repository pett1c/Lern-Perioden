import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from config import BOT_TOKEN
from data.database import init_db
from handlers import common, admin, economics, ai
from middlewares.logging_middleware import LoggingMiddleware

# Set up logging
logging.basicConfig(level=logging.INFO)

async def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN is not set.")
        return

    # initialize db
    await init_db()
    
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    
    # middleware
    dp.update.middleware(LoggingMiddleware())

    # include routers
    dp.include_router(admin.router) # admin, specialized
    dp.include_router(ai.router)
    dp.include_router(economics.router)
    dp.include_router(common.router) # common, catch-all

    print("Starting bot...")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"🛑 CRITICAL ERROR: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")