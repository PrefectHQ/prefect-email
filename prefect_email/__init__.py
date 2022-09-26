from . import _version
from .credentials import EmailServerCredentials, SMTPServer, SMTPType
from .message import email_send_message

__version__ = _version.get_versions()["version"]

__all__ = ["EmailServerCredentials", "SMTPServer", "SMTPType", "email_send_message"]
