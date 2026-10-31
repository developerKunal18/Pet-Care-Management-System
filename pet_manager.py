from storage import load_pets, save_pets
from utils import (
    get_text,
    get_positive_integer,
    current_datetime
)


def generate_pet_id(pets):
    highest = 0

    for pet in pets:
        pet_id = pet.get("pet_id", "")

        if pet_id.startswith("PET"):
            try:
                highest = max(highest, int(pet_id[3:]))
            except ValueError:
                continue

    return f"PET{highest + 1:04d}"


def find_pet(pets, pet_id):
    for pet in pets:
        if pet.get("pet_id", "").upper() == pet_id.upper():
            return pet

    return None


def add_pet():
    pets = load_pets()

    print("\n--- Register New Pet ---")

    name = get_text("Pet name: ")
    pet_type = get_text("Pet type (Dog, Cat, Bird, etc.): ")
    breed = get_text("Breed: ")
    age = get_positive_integer("Age in years: ")
    owner = get_text("Owner name: ")
    phone = get_text("Owner phone number: ")

    pet = {
        "pet_id": generate_pet_id(pets),
        "name": name,
        "pet_type": pet_type,
        "breed": breed,
        "age": age,
        "owner": owner,
        "phone": phone,
        "created_at": current_datetime()
    }

    pets.append(pet)
    save_pets(pets)

    print("\nPet registered successfully!")
    print(f"Pet ID: {pet['pet_id']}")


def display_pet(pet):
    print("-" * 42)
    print(f"Pet ID   : {pet['pet_id']}")
    print(f"Name     : {pet['name']}")
    print(f"Type     : {pet['pet_type']}")
    print(f"Breed    : {pet['breed']}")
    print(f"Age      : {pet['age']} year(s)")
    print(f"Owner    : {pet['owner']}")
    print(f"Phone    : {pet['phone']}")
    print("-" * 42)


def view_all_pets():
    pets = load_pets()

    print("\n--- Registered Pets ---")

    if not pets:
        print("No pets registered.")
        return

    for pet in pets:
        display_pet(pet)

    print(f"Total pets: {len(pets)}")


def search_pet():
    pets = load_pets()

    keyword = input(
        "Search by pet ID, name, breed, or owner: "
    ).strip().lower()

    if not keyword:
        print("Enter a search value.")
        return

    results = [
        pet for pet in pets
        if keyword in pet.get("pet_id", "").lower()
        or keyword in pet.get("name", "").lower()
        or keyword in pet.get("breed", "").lower()
        or keyword in pet.get("owner", "").lower()
    ]

    if not results:
        print("No matching pets found.")
        return

    for pet in results:
        display_pet(pet)


def edit_pet():
    pets = load_pets()
    pet_id = input("Enter pet ID to edit: ").strip().upper()

    pet = find_pet(pets, pet_id)

    if not pet:
        print("Pet not found.")
        return

    print("Leave a field blank to keep its current value.")

    fields = [
        ("name", "Pet name"),
        ("pet_type", "Pet type"),
        ("breed", "Breed"),
        ("owner", "Owner name"),
        ("phone", "Owner phone")
    ]

    for key, label in fields:
        value = input(f"{label} [{pet[key]}]: ").strip()

        if value:
            pet[key] = value

    age = input(f"Age [{pet['age']}]: ").strip()

    if age:
        try:
            new_age = int(age)

            if new_age < 0:
                print("Age cannot be negative. Keeping old age.")
            else:
                pet["age"] = new_age

        except ValueError:
            print("Invalid age. Keeping old age.")

    pet["updated_at"] = current_datetime()

    save_pets(pets)
    print("Pet details updated successfully.")


def delete_pet():
    pets = load_pets()
    pet_id = input("Enter pet ID to delete: ").strip().upper()

    pet = find_pet(pets, pet_id)

    if not pet:
        print("Pet not found.")
        return

    display_pet(pet)

    confirm = input("Delete this pet? (y/n): ").strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    # Keep care history instead of deleting it.
    pets.remove(pet)
    save_pets(pets)

    print("Pet deleted successfully.")
