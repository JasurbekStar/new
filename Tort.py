import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API = "7634215367:AAHRpe_QBIaP1adGgxanbxFMxTpTDYpqAEk"
dp = Dispatcher()
@dp.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.answer(f"Assalomu allekum, "
                         f"{message.from_user.full_name}!")

@dp.message()
async def message_handler(message: Message):
        await message.answer(message.text)

async def main():
    bot = Bot(token=API)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
