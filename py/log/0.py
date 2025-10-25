import logging

logger = logging.Logger(__name__)


logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)
logging.debug("debug logging")
logging.info("info logging")
logger.debug("debug")
logger.info("info")
logger.warning("warn")
logger.error("error")
logger.critical("critical")
