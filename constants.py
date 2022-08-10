import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

DT_FORMAT = "%Y-%m-%d_%H-%M-%S"

PATTERN = re.compile("^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)")

EXPECTED_STATUS = {
    'A': ['Active', 'Accepted'],
    'D': ['Deferred'],
    'F': ['Final'],
    'P': ['Provisional'],
    'R': ['Rejected'],
    'S': ['Superseded'],
    'W': ['Withdrawn'],
    '': ['Draft', 'Active'],
}
