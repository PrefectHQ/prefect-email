"""Credential classes used to perform authenticated interactions with email services"""

from typing import Union, Dict

import functools
import ssl
from enum import Enum
from dataclasses import dataclass
from smtplib import SMTP_SSL, SMTP


class SMTPType(Enum):
    SSL = 465
    STARTTLS = 465
    INSECURE = 25


class SMTPServer(Enum):
    AOL = "smtp.aol.com"
    ATT = "smtp.mail.att.net"
    COMCAST = "smtp.comcast.net"
    ICLOUD = "smtp.mail.me.com"
    GMAIL = "smtp.gmail.com"
    OUTLOOK = "smtp-mail.outlook.com"
    YAHOO = "smtp.mail.yahoo.com"


def _cast_to_enum(obj: Union[str, SMTPType], enum: Enum, valid_map: Dict[str, Enum] = None):
    """
    Casts string to an enum member, if valid.

    Args:
        obj: a member's name of the enum.
        enum: an Enum class.
        valid_map: valid mapping of the enum's values to its names.

    Returns:
        A member of the enum.
    """
    valid_map = valid_map or {}
    if isinstance(obj, enum):
        # if already an enum member, continue
        return obj
    elif obj in valid_map:
        # if the value (smtp.gmail.com) of an enum member (GMAIL)
        # is used as input, map it back to use the enum member
        return valid_map[obj]

    # capitalize and try to match an enum member
    obj = obj.upper()
    if not hasattr(enum, obj):
        valid_enums = list(enum.__members__)
        raise ValueError(
            f"Must be either {valid_enums}; got {obj}"
        )
    else:
        return getattr(enum, obj)


@dataclass
class EmailCredentials:
    """
    Dataclass used to manage generic email authentication. It is recommended you use a
    [Google App Password](https://support.google.com/accounts/answer/185833) if you use Gmail.

    Args:
        username: The username to use for authentication to the server.
        password: The password to use for authentication to the server.
        smtp_server: Either the hostname of the SMTP server or the service name like "gmail".
        smtp_type: Either "SSL", "STARTTLS", or "INSECURE".

    Returns:
        An authenticated SMTP server.
    
    Example:
        @flow
        def example_email_send_message_flow():
            email_credentials = EmailCredentials(
                username="username@email.com",
                password="password",
            )
            server = email_credentials.get_server()
            return server
    """

    username: str
    password: str
    smtp_server: Union[str, SMTPServer] = SMTPServer.GMAIL
    smtp_type: Union[str, SMTPType] = SMTPType.SSL

    def get_server(self) -> SMTP:
        smtp_server = _cast_to_enum(
            self.smtp_server,
            SMTPServer,
            valid_map=SMTPServer._value2member_map_
        ).value
        smtp_type = _cast_to_enum(self.smtp_type, SMTPType)
        smtp_port = smtp_type.value

        if smtp_type == SMTPType.INSECURE:
            server = SMTP(smtp_server, smtp_port)
        else:
            context = ssl.create_default_context()
            if smtp_type == SMTPType.SSL:
                server = SMTP_SSL(smtp_server, smtp_port, context=context)
            elif smtp_type == SMTPType.STARTTLS:
                server = SMTP(smtp_server, smtp_port)
                server.starttls(context=context)
            server.login(self.username, self.password)

        return server
