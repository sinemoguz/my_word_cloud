import logging


def initialize_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # create console handler and set level to info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
