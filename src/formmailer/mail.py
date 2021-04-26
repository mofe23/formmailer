import logging
import smtplib
import sys
import typing
from email.message import EmailMessage

from pydantic import NameEmail

logger = logging.getLogger(__name__)


def compose(
    *, recipients: typing.List[NameEmail], subject: str, content: str, sender: NameEmail
) -> EmailMessage:
    email = EmailMessage()
    email.set_content(content)

    email["Subject"] = subject
    email["From"] = str(sender)
    email["To"] = str(recipients[0])

    return email


def send(email: EmailMessage):
    if sys.platform == "darwin":
        logger.info(str(email))
    else:
        s = smtplib.SMTP("mail")
        s.send_message(email)
        s.quit()
