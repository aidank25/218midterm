import logging.handlers
import pytest
import os
import logging.config
import logging
from app.logger import setup_logger

setup_logger()

def test_logging_info(caplog):
    with caplog.at_level(logging.INFO):
        logging.info("test info")
    assert "test info" in caplog.text

def test_logging_error(caplog):
    with caplog.at_level(logging.ERROR):
        logging.error("test error")
    assert "test error" in caplog.text