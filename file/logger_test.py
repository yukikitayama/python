import logging

root_logger = logging.getLogger()
hello_logger = logging.getLogger("hello")
hello_world_logger = logging.getLogger("hello.world")
module_logger = logging.getLogger(__name__)
