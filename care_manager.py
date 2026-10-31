from datetime import date

from config import CARE_TYPES
from storage import load_pets, load_care_records, save_care_records
from pet_manager import find_pet
from utils import (
    get_text,
    get_date,
    get_optional_date,
    get_choice,
    current_datetime
)


def generate_care_id(records):
    highest = 0

    for record in records:
        care_id = record.get("care_id", "")

        if care_id.startswith("CARE"):
            try:
                highest = max(highest, int(care_id[4:]))
            except ValueError:
                continue

    return f"CARE{highest + 1:04d}"


def add_care_record():
    pets = load_pets()
    records = load_care_records()

    if not pets:
        print("Register a pet before adding care records.")
        return

    print("\n--- Add Pet Care Record ---")

    for pet in pets:
        print(f"{pet['pet_id']} - {pet['name']} ({pet['pet_type']})")

    pet_id = input("Enter pet ID: ").strip().upper()
    pet = find_pet(pets, pet_id)

    if not pet:
        print("Pet not found.")
        return

    care_type = get_choice("Select care activity: ", CARE_TYPES)
    description = get_text("Description: ")
    care_date = get_date("Activity date (YYYY-MM-DD): ")
    next_due = get_optional_date(
        "Next due date (YYYY-MM-DD, optional): "
    )

    if next_due and next_due < care_date:
        print("Next due date cannot be earlier than the activity date.")
        return

    record = {
        "care_id": generate_care_id(records),
        "pet_id": pet["pet_id"],
        "pet_name": pet["name"],
        "care_type": care_type,
        "description": description,
        "care_date": care_date,
        "next_due": next_due,
        "status": "Completed" if care_date <= date.today().isoformat()
                  else "Scheduled",
        "created_at": current_datetime()
    }

    records.append(record)
    save_care_records(records)

    print("\nCare record added successfully!")
    print(f"Care ID: {record['care_id']}")


def display_care_record(record):
    print("-" * 45)
    print(f"Care ID     : {record['care_id']}")
    print(f"Pet ID      : {record['pet_id']}")
    print(f"Pet Name    : {record['pet_name']}")
    print(f"Care Type   : {record['care_type']}")
    print(f"Description : {record['description']}")
    print(f"Activity Date: {record['care_date']}")
    print(f"Next Due    : {record.get('next_due') or 'Not specified'}")
    print(f"Status      : {record['status']}")
    print("-" * 45)


def view_all_care_records():
    records = load_care_records()

    print("\n--- All Pet Care Records ---")

    if not records:
        print("No care records found.")
        return

    records.sort(key=lambda item: item.get("care_date", ""), reverse=True)

    for record in records:
        display_care_record(record)

    print(f"Total care records: {len(records)}")


def view_pet_care_history():
    records = load_care_records()

    pet_id = input("Enter pet ID: ").strip().upper()

    results = [
        record for record in records
        if record.get("pet_id", "").upper() == pet_id
    ]

    if not results:
        print("No care history found for this pet.")
        return

    print(f"\n--- Care History for {results[0]['pet_name']} ---")

    for record in sorted(
        results,
        key=lambda item: item.get("care_date", ""),
        reverse=True
    ):
        display_care_record(record)


def view_upcoming_care():
    records = load_care_records()
    today = date.today().isoformat()

    upcoming = [
        record for record in records
        if record.get("status") == "Scheduled"
        and record.get("next_due")
        and record["next_due"] >= today
    ]

    upcoming.sort(key=lambda item: item["next_due"])

    print("\n--- Upcoming Care Activities ---")

    if not upcoming:
        print("No upcoming care activities found.")
        return

    for record in upcoming:
        display_care_record(record)


def complete_care_record():
    records = load_care_records()
    care_id = input("Enter care ID: ").strip().upper()

    for record in records:
        if record.get("care_id", "").upper() == care_id:
            if record["status"] == "Completed":
                print("This activity is already completed.")
                return

            record["status"] = "Completed"
            record["completed_at"] = current_datetime()

            save_care_records(records)

            print("Care activity marked as completed.")
            return

    print("Care record not found.")


def delete_care_record():
    records = load_care_records()
    care_id = input("Enter care ID to delete: ").strip().upper()

    for record in records:
        if record.get("care_id", "").upper() == care_id:
            display_care_record(record)

            confirm = input("Delete this care record? (y/n): ").strip().lower()

            if confirm == "y":
                records.remove(record)
                save_care_records(records)
                print("Care record deleted.")
            else:
                print("Deletion cancelled.")

            return

    print("Care record not found.")
