"""
Initial setup for app.
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

if not app.debug:
    # log errors to file when not running in debug mode
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler("tmp/viz-alg.log", "a", 1024**2, 10)

    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))

    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)

    app.logger.info("app started")
