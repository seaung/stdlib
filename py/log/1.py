import logging


logging.basicConfig(filename="log.txt", filemode="w", datefmt="%m-%d-%Y-%I:%M:%S %p", format="%(levelname)s - %(asctime)s - %(message)s")
logging.info("info logging")
logging.warning("warning logging")
