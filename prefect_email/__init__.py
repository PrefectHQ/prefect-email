from . import _version
from .credentials import SMTPType, SMTPServer, EmailServerCredentials  # noqa
from .message import email_send_message  # noqa

__version__ = _version.get_versions()["version"]
