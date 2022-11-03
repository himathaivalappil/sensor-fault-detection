import logging
import os
import datetime
from from_root import from_root

LOG_FILE = f"{datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(from_root(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level = logging.INFO,
    format="[%(asctime)s] - %(lineno)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode='w'),
        logging.StreamHandler()
    ]
)