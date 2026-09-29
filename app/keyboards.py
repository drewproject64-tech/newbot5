from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

UPPERCASE = "Uppercase"
LOWERCASE = "Lowercase"
TITLE_CASE = "Title Case"

def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=UPPERCASE)],
            [KeyboardButton(text=LOWERCASE)],
            [KeyboardButton(text=TITLE_CASE)],
        ],
        resize_keyboard=True,
        input_field_placeholder="Choose a case tool",
    )
