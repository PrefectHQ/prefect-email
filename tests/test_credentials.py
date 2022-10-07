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
@pytest.mark.parametrize(
    "smtp_type, smtp_port",
    [("SSL", 465), ("STARTTLS", 587), ("ssl", 465), ("StartTLS", 587)],
)
def test_email_server_credentials_get_server(smtp_server, smtp_type, smtp_port, smtp):
    server = EmailServerCredentials(
        username="username",
        password="password",
        smtp_server=smtp_server,
        smtp_type=smtp_type,
    ).get_server()
    assert server.username == "username"
    assert server.password == "password"
    assert server.server.lower() == "smtp.gmail.com"
    assert server.port == smtp_port


def test_email_server_credentials_get_server_error(smtp):
    with pytest.raises(ValueError):
        EmailServerCredentials(
            username="username", password="password", smtp_type="INVALID"
        ).get_server()
