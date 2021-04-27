import json
import logging
import smtplib
import typing

import pydantic
from bottle import HTTPResponse, default_app, request
from pydantic import BaseModel, EmailStr, NameEmail, constr

from . import mail
from .settings import Config

logger = logging.getLogger(__name__)
app = default_app()


class ContactForm(BaseModel):
    email: EmailStr
    name: constr(max_length=100, min_length=2)
    subject: constr(min_length=2)
    message: constr(min_length=10)
    company: typing.Optional[str] = None

    class Config:
        validate_all = True
        anystr_strip_whitespace = True

    @property
    def recipient(self) -> NameEmail:
        return NameEmail(self.name, self.email)


def error_response(
    errors: typing.List[typing.Any], status: int = 400, exception: Exception = None
) -> HTTPResponse:
    return HTTPResponse(
        body=json.dumps(
            {"errors": errors}, default=pydantic.error_wrappers.pydantic_encoder
        ),
        status=status,
        exception=repr(exception),
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    )


def validation_error_response(exception: pydantic.ValidationError):
    return error_response(exception.errors(), status=400, exception=exception)


@app.post("/")
def send_email():
    client_ip = request.environ.get("REMOTE_ADDR")
    logger.info(f"Received form from {client_ip}")

    try:
        form = ContactForm(
            **{
                field: request.forms.getunicode(field, None)
                for field in ContactForm.__fields__
            }
        )
    except pydantic.ValidationError as e:
        logger.error(f"Invalid form: {e}")
        return validation_error_response(e)

    try:
        cfg = Config()
        email = mail.compose(
            content=form.message,
            subject=form.subject,
            reply_to=form.recipient,
            recipients=cfg.recipient,
            sender=cfg.sender,
        )
        mail.send(email)
    except smtplib.SMTPException as e:
        logger.exception(f"Failed to send mail to {form.recipient}")
        return error_response(errors=[str(e)], status=500, exception=e)

    return HTTPResponse(status=200)
