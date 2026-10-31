from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

PETS_FILE = DATA_DIR / "pets.json"
CARE_FILE = DATA_DIR / "care_records.json"

DATE_FORMAT = "%Y-%m-%d"

CARE_TYPES = [
    "Feeding",
    "Vaccination",
    "Grooming",
    "Medical Visit",
    "Medication",
    "Other"
]
