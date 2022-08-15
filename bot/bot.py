#!/usr/bin/env python3

"""Bot implementation."""

import datetime
import json
import logging
import time
import unittest
from pathlib import Path
from typing import Any, Callable, List, Optional, Union

import telegram

try:
    from typing_extensions import TypedDict
except ImportError:
    from typing import TypedDict

from telegram_menu import BaseMessage, ButtonType, MenuButton, NavigationHandler, TelegramMenuSession
from telegram_menu._version import __raw_url__