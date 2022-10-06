import ssl

import pytest

from prefect_email.credentials import (
    EmailServerCredentials,
    SMTPServer,
    SMTPType,
    _cast_to_enum,
)


@pytest.mark.parametrize("obj", ["gmail", "Gmail", "GMAIL", SMTPServer.GMAIL])
def test_cast_to_enum(obj):
    assert _cast_to_enum(obj, SMTPServer, restrict=False) == SMTPServer.GMAIL


@pytest.mark.parametrize("obj", ["smtp.prefect.io", "smtp.gmail.com"])
def test_cast_to_enum_no_restrict_server(obj):
    assert _cast_to_enum(obj, SMTPServer, restrict=False) == obj


@pytest.mark.parametrize("obj", ["ssl", "Ssl", "SSL", SMTPType.SSL])
def test_cast_to_enum_restrict_type(obj):
    assert _cast_to_enum(obj, SMTPType, restrict=True) == SMTPType.SSL


def test_cast_to_enum_restrict_error():
    with pytest.raises(ValueError):
        _cast_to_enum("Invalid", SMTPType, restrict=True)


@pytest.mark.parametrize(
    "smtp_server", ["gmail", "GMAIL", "smtp.gmail.com", "SMTP.GMAIL.COM"]
)
@pytest.mark.parametrize("smtp_type", ["SSL", "STARTTLS", "ssl", "StartTLS"])
@pytest.mark.parametrize("ssl_context", [None, ssl.create_default_context()])
def test_email_server_credentials_get_server(smtp_server, smtp_type, smtp, ssl_context):
    server = EmailServerCredentials(
        username="username",
        password="password",
        smtp_server=smtp_server,
        smtp_type=smtp_type,
    ).get_server(ssl_context=ssl_context)
    assert server.username == "username"
    assert server.password == "password"
    assert server.server.lower() == "smtp.gmail.com"
    assert server.port == 465
    default_context = ssl.create_default_context()
    assert server.context.protocol == default_context.protocol
    assert server.context.options == default_context.options
    assert server.context.get_ciphers() == default_context.get_ciphers()
    assert server.context.verify_flags == default_context.verify_flags


def test_email_server_credentials_get_server_custom_context(smtp):
    custom_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
    custom_context.options = ssl.OP_NO_TICKET
    server = EmailServerCredentials(
        username="username",
        password="password",
    ).get_server(ssl_context=custom_context)
    assert server.username == "username"
    assert server.password == "password"
    assert server.server.lower() == "smtp.gmail.com"
    assert server.port == 465
    assert server.context.protocol == custom_context.protocol
    assert server.context.options == custom_context.options


def test_email_server_credentials_get_server_error(smtp):
    with pytest.raises(ValueError):
        EmailServerCredentials(
            username="username", password="password", smtp_type="INVALID"
        ).get_server()
