import logging
import os
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"    # logs folder for storing logs..
log_filepath = os.path.join(log_dir, "logging.log") # Path: logs/logging.log

os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.FileHandler(log_filepath),  # Content in file
        logging.StreamHandler(sys.stdout) # We can see the content in terminal also.
    ]
)

logger = logging.getLogger("datasciencelogger")