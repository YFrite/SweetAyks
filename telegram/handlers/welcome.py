from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

welcome = Router()


@welcome.message(Command("pong"))
async def start(message: Message):
    await message.answer("Ping!")
