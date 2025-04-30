import logging
from pathlib import Path

# Create logs directory
Path("logs").mkdir(exist_ok=True)

# Configure root logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Application started")
    try:
        1 / 0
    except Exception:
        logger.exception("Critical error occurred")

if __name__ == "__main__":
    main()