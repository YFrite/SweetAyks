import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from settings import settings
from telegram.handlers.welcome import welcome


async def main():
    bot = Bot(settings.bot_token)
    dp = Dispatcher()

    dp.include_router(welcome)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.get_event_loop().run_until_complete(main())
