# Discord Cleanup Bot

A simple Discord bot that cleans up your messages. Because I am a lazy person,  
I don't want to manually delete messages every time I want to clean up my channels.

## Commands

- `!status`: Get the bot's current status.
- `!clean <time>`: Clean up messages in a channel until the specified time.  
  See also [dateparser](https://dateparser.readthedocs.io/en/latest/) that powers
  the time input parsing (i.e. `today` or `tomorrow` are valid inputs).

## Setup Instructions

1. Create a Discord bot and get its token. Message Content Intent is required.  
2. Add the bot to your server and give it the `Manage Messages` & `Send Messages`  
permissions.

## Docker execution

You can run the bot using Docker (see also [docker-compose.yaml](./examples/docker-compose.yaml)).

```bash
docker run -e DISCORD_BOT_TOKEN=<your-bot-token> \
  ghcr.io/violetcranberry/discord-cleanup-bot:latest
```
