import functools
import typing

from pydantic import BaseSettings, NameEmail


def singleton(cls):
    previous_instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls in previous_instances and previous_instances.get(cls, None).get(
            "args"
        ) == (args, kwargs):
            return previous_instances[cls].get("instance")
        else:
            previous_instances[cls] = {
                "args": (args, kwargs),
                "instance": cls(*args, **kwargs),
            }
            return previous_instances[cls].get("instance")

    return wrapper


@singleton
class Config(BaseSettings):
    listen: str = "0.0.0.0"
    port: int = 8080
    debug: bool = False
    sender: NameEmail = "FormMailer Sender <sender@formmailer.io>"
    recipient: NameEmail = "FormMailer Recipient <recipient@formmailer.io>"
    smtp_host: str = "mail"

    __instance__: typing.Optional["Config"] = None

    class Config:
        case_sensitive = False
        env_prefix = "FORMMAILER_"  # defaults to no prefix, i.e. ""
