import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web
import os

# هذي عشان ياخذ المنفذ اللي يحدده Render تلقائياً
PORT = int(os.environ.get("PORT", 8080))

# باقي الكود حقك
from config import BOT_TOKEN
from common import router as common_router
from generate import router as generate_router
from admin import router as admin_router
from chat import router as chat_router

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(admin_router)
dp.include_router(common_router)
dp.include_router(generate_router)
dp.include_router(chat_router)

async def start_server():
    app = web.Application()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    print(f"Server started on port {PORT}")

async def main():
    await start_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
