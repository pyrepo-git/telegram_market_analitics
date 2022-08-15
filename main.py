#!/usr/bin/env python3

"""telegram_menu demonstrator."""

import logging
from pathlib import Path

from telegram_menu import TelegramMenuSession
from tests.test_connection import MyNavigationHandler, StartMessage, init_logger


def run() -> None:
    """Run the demo example."""
    init_logger()
    # with (Path.home() / ".telegram_menu" / "key.txt").open() as key_h:
    with (Path(".") / "key.txt").open() as key_h:
        api_key = key_h.read().strip()

    logging.info(" >> Start the demo and wait forever, quit with CTRL+C...")
    TelegramMenuSession(api_key).start(
        start_message_class=StartMessage, navigation_handler_class=MyNavigationHandler, idle=True
    )


if __name__ == "__main__":
    run()
