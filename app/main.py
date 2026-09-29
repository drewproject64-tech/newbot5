import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest

from .config import load_settings
from .handlers import router

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

async def configure_profile(bot: Bot, settings) -> None:
    await bot.set_my_name(name=settings.bot_name)
    await bot.set_my_short_description(short_description=settings.bot_about)
    await bot.set_my_description(description=settings.bot_description)

async def main():
    settings = load_settings()
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    bot._sb24_modes = {}
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await configure_profile(bot, settings)
    except TelegramBadRequest as exc:
        logging.getLogger(__name__).warning("Profile configuration warning: %s", exc)
    logging.info("Starting %s (%s)", settings.bot_name, settings.bot_username)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
