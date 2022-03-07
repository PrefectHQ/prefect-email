from unittest.mock import MagicMock

import pytest


class EmailServerMethodsMock:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def send_message(self, message):
        return message


@pytest.fixture
def email_credentials():
    email_credentials = MagicMock(username="someone@email.com")
    email_credentials.get_server.side_effect = lambda: EmailServerMethodsMock()
    return email_credentials
