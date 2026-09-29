from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from .keyboards import LOWERCASE, TITLE_CASE, UPPERCASE, main_menu

router = Router()
WELCOME = (
    "Welcome to SB24 Bot.\n\n"
    "Convert your text into the case you need:\n"
    "• Uppercase\n• Lowercase\n• Title Case\n\n"
    "Choose a tool below, then send your text."
)
PROMPTS = {
    UPPERCASE: "Send the text you want converted to UPPERCASE.",
    LOWERCASE: "Send the text you want converted to lowercase.",
    TITLE_CASE: "Send the text you want converted to Title Case.",
}

def _mode_store(bot):
    if not hasattr(bot, "_sb24_modes"):
        bot._sb24_modes = {}
    return bot._sb24_modes

@router.message(CommandStart())
async def start_handler(message: Message):
    _mode_store(message.bot).pop(message.from_user.id, None)
    await message.answer(WELCOME, reply_markup=main_menu())

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Choose one of the three case tools, then send the text you want to convert.",
        reply_markup=main_menu(),
    )

@router.message(F.text.in_({UPPERCASE, LOWERCASE, TITLE_CASE}))
async def case_tool_handler(message: Message):
    _mode_store(message.bot)[message.from_user.id] = message.text
    await message.answer(PROMPTS[message.text], reply_markup=main_menu())

@router.message(F.text)
async def text_handler(message: Message):
    mode = _mode_store(message.bot).get(message.from_user.id)
    if not mode:
        await message.answer(
            "Please choose one of the three case tools first.",
            reply_markup=main_menu(),
        )
        return
    text = message.text
    if not text.strip():
        await message.answer("Please send some text to convert.", reply_markup=main_menu())
        return
    if mode == UPPERCASE:
        result = text.upper()
    elif mode == LOWERCASE:
        result = text.lower()
    elif mode == TITLE_CASE:
        result = text.title()
    else:
        _mode_store(message.bot).pop(message.from_user.id, None)
        await message.answer("Please choose a case tool again.", reply_markup=main_menu())
        return
    if len(result) > 4000:
        await message.answer(
            "That text is too long to return in one Telegram message. Please send a shorter text.",
            reply_markup=main_menu(),
        )
        return
    await message.answer(result, reply_markup=main_menu())

@router.message()
async def unsupported_message_handler(message: Message):
    await message.answer(
        "I can convert text to Uppercase, Lowercase, or Title Case. "
        "Choose one of the three tools below.",
        reply_markup=main_menu(),
    )
