import pytest

from prefect_email.credentials import (
    EmailCredentials,
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
def test_email_credentials_get_server(smtp_server, smtp_type, smtp):
    server = EmailCredentials(
        "username", "password", smtp_server=smtp_server, smtp_type=smtp_type
    ).get_server()
    assert server.username == "username"
    assert server.password == "password"
    assert server.server.lower() == "smtp.gmail.com"
    assert server.port == 465


def test_email_credentials_get_server_error(smtp):
    with pytest.raises(ValueError):
        EmailCredentials("username", "password", smtp_type="INVALID").get_server()
