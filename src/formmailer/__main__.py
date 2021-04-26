import logging
import pathlib
import sys

from bottle import run

logger = logging.getLogger(__name__)


def main():
    from formmailer.server import app
    from formmailer.settings import Config

    config = Config()
    logging.basicConfig(level=logging.INFO)
    mode = " in debug mode" if config.debug else ""
    logger.info(f"Running formmail on {config.listen}:{config.port}{mode}")
    run(
        app=app,
        reloader=config.debug,
        debug=config.debug,
        host=config.listen,
        port=config.port,
    )


if __name__ == "__main__":
    p = pathlib.Path(__file__).parent.parent.absolute()
    if str(p) not in sys.path:
        sys.path.append(str(p))

    print(sys.path)
    sys.exit(main())
