import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("data_processor")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    "data.log",
    maxBytes=1024*1024,  # 1MB
    backupCount=3
)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

def process_record(record):
    try:
        logger.debug(f"Processing: {record}")
        if not record.is_valid():
            logger.warning("Invalid record format")
        # Processing logic here
    except Exception as e:
        logger.error(f"Failed to process record: {str(e)}", exc_info=True)