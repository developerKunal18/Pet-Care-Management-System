from collections import Counter
from datetime import date

from storage import load_pets, load_care_records
from config import CARE_TYPES


def pet_summary():
    pets = load_pets()
    records = load_care_records()

    print("\n========== PET SUMMARY ==========")
    print(f"Total registered pets: {len(pets)}")
    print(f"Total care records: {len(records)}")

    if records:
        completed = sum(
            1 for record in records
            if record.get("status") == "Completed"
        )

        scheduled = sum(
            1 for record in records
            if record.get("status") == "Scheduled"
        )

        print(f"Completed activities: {completed}")
        print(f"Scheduled activities: {scheduled}")

    print("=" * 35)


def care_type_report():
    records = load_care_records()

    if not records:
        print("No care records available.")
        return

    counts = Counter(
        record.get("care_type", "Other")
        for record in records
    )

    print("\n--- Care Activities by Type ---")

    for care_type in CARE_TYPES:
        print(f"{care_type}: {counts.get(care_type, 0)}")

    print(f"Total activities: {len(records)}")


def pet_wise_report():
    pets = load_pets()
    records = load_care_records()

    if not pets:
        print("No registered pets found.")
        return

    print("\n--- Pet-Wise Care Report ---")

    for pet in pets:
        pet_records = [
            record for record in records
            if record.get("pet_id") == pet["pet_id"]
        ]

        completed = sum(
            1 for record in pet_records
            if record.get("status") == "Completed"
        )

        scheduled = sum(
            1 for record in pet_records
            if record.get("status") == "Scheduled"
        )

        print(
            f"{pet['name']} | "
            f"Total: {len(pet_records)} | "
            f"Completed: {completed} | "
            f"Scheduled: {scheduled}"
        )


def overdue_care_report():
    records = load_care_records()
    today = date.today().isoformat()

    overdue = [
        record for record in records
        if record.get("status") == "Scheduled"
        and record.get("next_due")
        and record["next_due"] < today
    ]

    print("\n--- Overdue Care Activities ---")

    if not overdue:
        print("No overdue care activities.")
        return

    for record in overdue:
        print(
            f"{record['care_id']} | "
            f"{record['pet_name']} | "
            f"{record['care_type']} | "
            f"Due: {record['next_due']}"
        )
