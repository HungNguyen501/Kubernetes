"""Streaming Job Example"""
from datetime import datetime
from time import sleep
import os

from faker import Faker
from loguru import logger


fake = Faker()


def mock_call_data():
    return {
        "event_time": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
        "name": fake.name(),
        "email": fake.email(),
        "credentials": os.environ["CREDENTIALS"],
    }


if __name__ == "__main__":
    while True:
        logger.info(mock_call_data())
        sleep(60)
