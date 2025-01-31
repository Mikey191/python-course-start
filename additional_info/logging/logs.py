import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def div(n1, n2):
    logger.info("run div")

    if n2 == 0:
        logger.error(f'n2 must be biggest zero')


div(5, 0)