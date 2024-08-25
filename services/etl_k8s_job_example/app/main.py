"""ETL Job"""
from datetime import datetime
import os

from faker import Faker
from loguru import logger


fake = Faker()


def mock_call_data():
    return {
        "event_date": datetime.strftime(datetime.now(), "%Y-%m-%d"),
        "name": fake.name(),
        "email": fake.email(),
        "credentials": os.environ["CREDENTIALS"],
    }


if __name__ == "__main__":
    logger.info(mock_call_data())
