import argparse
import logging

from discord_cleanup_bot.utils import get_arguments, get_bot_token
from discord_cleanup_bot.bot import bot


def main() -> None:
    """Main function."""
    args: argparse.Namespace = get_arguments()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.getLogger("discord").setLevel(
        logging.DEBUG if args.debug else logging.INFO
    )

    try:
        bot_token: str = get_bot_token(args)
    except ValueError as err:
        logging.error(err)
        exit(1)

    bot.run(bot_token, root_logger=True)


if __name__ == "__main__":
    main()
