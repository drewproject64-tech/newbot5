# SB24 Bot — @GZCaseFlipBot

SB24 Bot is a self-contained Telegram text case converter.

## Exactly 3 main buttons
- Uppercase
- Lowercase
- Title Case

## Setup
1. Install Python 3.12+.
2. Run `pip install -r requirements.txt`.
3. Set `BOT_TOKEN` as an environment variable.
4. Run `python -m app.main`.

## Render
Deploy as a background worker using the included `render.yaml` and set `BOT_TOKEN` as a secret environment variable.

The bot configures its name, About, and Description at startup where the Bot API permits it. The username remains managed through BotFather.

No external links, redirects, gambling, casino, betting, payment, or unrelated features are included.

Telegram Ads approval is not guaranteed; moderation decisions remain with Telegram.
