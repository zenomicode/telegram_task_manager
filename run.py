from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


load_dotenv()

async def main() -> None:
    bot = Bot(os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())

