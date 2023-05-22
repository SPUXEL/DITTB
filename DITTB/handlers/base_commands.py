
from aiogram.types import Message

from api import bot, dispatcher


@dispatcher.message_handler(
    commands=["start"]
)
async def command_start(update: Message):
    await update.answer("Work!")
