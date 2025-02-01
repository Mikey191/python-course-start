import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def div(n1, n2):
    logger.info("run div")

    if n2 == 0:
        logger.error(f'n2 must be biggest zero')
        return None
    return 


div(5, 0)