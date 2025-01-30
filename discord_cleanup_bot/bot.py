import logging
import discord

from discord.ext import commands
from discord_cleanup_bot.utils import parse_time_input


def init_bot_instance(description: str) -> commands.Bot:
    """Initialize the bot instance."""
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    return commands.Bot(
        command_prefix="!", intents=intents, description=description
    )


bot = init_bot_instance(description="Discord Cleanup Bot")


@bot.event
async def on_ready() -> None:
    logging.info(
        f"Logged in as {bot.user} (ID: {bot.user.id})"  # pyright: ignore[reportOptionalMemberAccess]
    )


@bot.command(description="Get the bot's current status.")
async def status(ctx: commands.Context) -> None:
    """Get the bot's current status."""
    logging.info(
        f"Status command requested by {ctx.author} in channel #{ctx.channel.name} (ID: {ctx.channel.id})"  # pyright: ignore[reportAttributeAccessIssue]
    )
    await ctx.send(f"I'm currently online and ready to serve.")


@bot.command(description="Clean up messages in a channel.")
@commands.has_permissions(manage_messages=True)
async def clean(ctx: commands.Context, *time_input: str) -> None:
    """Clean up messages in a channel."""
    logging.info(
        f"Clean command requested by {ctx.author} in channel #{ctx.channel.name} (ID: {ctx.channel.id})"  # pyright: ignore[reportAttributeAccessIssue]
    )
    try:
        threshold = parse_time_input(str(time_input))
        deleted = await ctx.channel.purge(  # pyright: ignore[reportAttributeAccessIssue]
            before=threshold,
            limit=1000,
        )
        logging.info(
            f"Deleted {len(deleted)} messages in channel #{ctx.channel.name} (ID: {ctx.channel.id})"  # pyright: ignore[reportAttributeAccessIssue]
        )
        await ctx.send(
            f"Deleted {len(deleted)} messages older than {threshold.strftime("%B %d, %Y")}."
        )
    except ValueError as err:
        await ctx.send(str(err))  # pyright: ignore[reportCallIssue]
        return
