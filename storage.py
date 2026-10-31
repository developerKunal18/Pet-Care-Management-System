import json
from config import DATA_DIR, PETS_FILE, CARE_FILE


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for file_path in [PETS_FILE, CARE_FILE]:
        if not file_path.exists():
            with file_path.open("w", encoding="utf-8") as file:
                json.dump([], file, indent=4)


def load_data(file_path):
    initialize_storage()

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except (OSError, json.JSONDecodeError) as error:
        print(f"Error reading {file_path.name}: {error}")
        return []


def save_data(file_path, data):
    initialize_storage()

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_pets():
    return load_data(PETS_FILE)


def save_pets(pets):
    save_data(PETS_FILE, pets)


def load_care_records():
    return load_data(CARE_FILE)


def save_care_records(records):
    save_data(CARE_FILE, records)
