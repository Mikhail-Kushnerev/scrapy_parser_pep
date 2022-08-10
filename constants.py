import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

DT_FORMAT = "%Y-%m-%d_%H-%M-%S"

PATTERN = re.compile(r"^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)")
