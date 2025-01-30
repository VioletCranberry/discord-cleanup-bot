from datetime import datetime

import unittest
from unittest.mock import patch
import argparse

from discord_cleanup_bot.utils import (
    get_bot_token,
    parse_time_input,
)


class TestGetBotToken(unittest.TestCase):
    @patch("os.getenv")
    def test_get_bot_token_from_args(self, mock_getenv):
        mock_args = argparse.Namespace(token="mock_token")
        mock_getenv.return_value = None  # No token in the environment
        token = get_bot_token(mock_args)
        self.assertEqual(token, "mock_token")

    @patch("os.getenv")
    def test_get_bot_token_from_env(self, mock_getenv):
        mock_args = argparse.Namespace(token=None)
        mock_getenv.return_value = "env_token"  # Token in the environment
        token = get_bot_token(mock_args)
        self.assertEqual(token, "env_token")

    @patch("os.getenv")
    def test_get_bot_token_not_provided(self, mock_getenv):
        mock_args = argparse.Namespace(token=None)
        mock_getenv.return_value = None  # No token in the environment
        with self.assertRaises(ValueError):
            get_bot_token(mock_args)


class TestParseTimeInput(unittest.TestCase):
    def test_parse_valid_time_input(self):
        time_input = "1st of January 2024 at 10:00"
        expected_datetime = datetime(2024, 1, 1, 10, 0, 0)
        parsed_date = parse_time_input(time_input)
        self.assertEqual(parsed_date, expected_datetime)

    def test_parse_relative_time_input(self):
        time_input = "tomorrow"
        parsed_date = parse_time_input(time_input)
        self.assertIsInstance(
            parsed_date, datetime
        )  # Check that it returns a datetime object

    def test_parse_invalid_time_input(self):
        time_input = "invalid-date-string"
        with self.assertRaises(ValueError):
            parse_time_input(time_input)
