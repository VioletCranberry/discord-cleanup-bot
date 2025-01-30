import argparse
import os
import logging

from datetime import datetime
import dateparser


def get_bot_token(args: argparse.Namespace) -> str:
    """Get the bot token from arguments or environment"""
    token_sources = [
        args.token,
        os.getenv("DISCORD_BOT_TOKEN"),
    ]
    for token in token_sources:
        if token:
            logging.debug(f"Found bot token: {token}")
            return token
    raise ValueError("Bot token was not provided.")


def parse_time_input(time_input: str) -> datetime:
    """
    Parses a time input string using dateparser and
    returns the corresponding datetime.
    """
    parsed_date = dateparser.parse(time_input)
    logging.info(f"Parsed time input: {parsed_date}")
    if not parsed_date:
        raise ValueError("Unable to parse the provided time input.")
    return parsed_date


def get_arguments() -> argparse.Namespace:
    """Parses and returns command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--token",
        action="store",
        help="Bot token (overrides env. variable).",
        required=False,
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Should we run the bot in debug mode?",
        required=False,
    )
    return parser.parse_args()
