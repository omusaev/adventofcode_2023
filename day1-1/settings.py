import logging
import sys

# create settings_local.py and redefine with an actual value
LOGGING_LEVEL = logging.INFO

CALIBRATION_DATA_FILENAME = "./data/calibration_data.txt"

try:
    from settings_local import *
except ImportError:
    pass

logger = logging.getLogger("adventofcode")
logger.setLevel(LOGGING_LEVEL)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(LOGGING_LEVEL)
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
