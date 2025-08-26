# conftest.py
import logging
import sys


def pytest_configure(config):
    # Configure uvicorn.error logger to stream to stdout
    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.INFO)  # Or DEBUG if needed
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
