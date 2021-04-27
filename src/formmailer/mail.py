import logging
import smtplib
import sys
from email.message import EmailMessage

from pydantic import NameEmail

logger = logging.getLogger(__name__)


def compose(
    *,
    content: str,
    subject: str,
    recipients: NameEmail,
    sender: NameEmail,
    reply_to: NameEmail,
) -> EmailMessage:
    email = EmailMessage()
    email.set_content(content)

    email["Subject"] = subject
    email["From"] = NameEmail(name=reply_to.name, email=sender.email)
    email["To"] = str(recipients)
    email["Reply-To"] = str(reply_to)

    return email


def send(email: EmailMessage):
    if sys.platform == "darwin":
        logger.info(str(email))
    else:
        s = smtplib.SMTP("mail")
        s.send_message(email)
        s.quit()
