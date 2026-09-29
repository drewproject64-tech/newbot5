"""Render-compatible entry point for SB24 Bot.

This file intentionally delegates to the production application in app.main.
It allows Render services configured with the legacy/default command
'python bot.py' to start correctly.
"""

import asyncio

from app.main import main


if __name__ == "__main__":
    asyncio.run(main())
