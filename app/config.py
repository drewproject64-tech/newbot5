import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    bot_token: str
    bot_name: str = "SB24 Bot"
    bot_username: str = "@GZCaseFlipBot"
    bot_about: str = "Convert text to uppercase, lowercase, or title case."
    bot_description: str = (
        "SB24 Bot is a simple text case converter. "
        "Choose Uppercase, Lowercase, or Title Case, then send your text."
    )

def load_settings() -> Settings:
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError("BOT_TOKEN is not set.")
    return Settings(
        bot_token=token,
        bot_name=os.getenv("BOT_NAME", "SB24 Bot").strip() or "SB24 Bot",
        bot_username=os.getenv("BOT_USERNAME", "@GZCaseFlipBot").strip() or "@GZCaseFlipBot",
        bot_about=os.getenv(
            "BOT_ABOUT",
            "Convert text to uppercase, lowercase, or title case.",
        ).strip(),
        bot_description=os.getenv(
            "BOT_DESCRIPTION",
            "SB24 Bot is a simple text case converter. "
            "Choose Uppercase, Lowercase, or Title Case, then send your text.",
        ).strip(),
    )
