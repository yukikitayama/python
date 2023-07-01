import logging

formatter = logging.Formatter("%(levelname)s %(asctime)s %(message)s")

handler = logging.FileHandler("config_prod.log", mode="a")
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)

logger.critical("critical")
logger.error("error")
logger.warning("warning")
logger.info("info")
logger.debug("debug")
