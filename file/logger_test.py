import logging

FORMAT = "%(levelname)s %(asctime)s %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    filename="prod.log",
    filemode="a"  # a means append
)

root_logger = logging.getLogger()
# root_logger.setLevel(logging.INFO)

hello_logger = logging.getLogger("hello")
hello_world_logger = logging.getLogger("hello.world")
module_logger = logging.getLogger(__name__)

# Default will print
root_logger.critical("critical")
root_logger.error("error")
root_logger.warning("warning")

# Default will not print
root_logger.info("info")
root_logger.debug("debug")
