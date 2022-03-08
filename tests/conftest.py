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


class SMTPMock:
    def __init__(self, server, port, context=None):
        self.server = server
        self.port = port
        self.context = context

    def login(self, username, password):
        self.username = username
        self.password = password


@pytest.fixture
def smtp(monkeypatch):
    monkeypatch.setattr("prefect_email.credentials.SMTP", SMTPMock)
    monkeypatch.setattr("prefect_email.credentials.SMTP_SSL", SMTPMock)
