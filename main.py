from storage import initialize_storage

from pet_manager import (
    add_pet,
    view_all_pets,
    search_pet,
    edit_pet,
    delete_pet
)

from care_manager import (
    add_care_record,
    view_all_care_records,
    view_pet_care_history,
    view_upcoming_care,
    complete_care_record,
    delete_care_record
)

from report_manager import (
    pet_summary,
    care_type_report,
    pet_wise_report,
    overdue_care_report
)

from utils import pause


def show_menu():
    print("\n" + "=" * 46)
    print("         PET CARE MANAGEMENT SYSTEM")
    print("=" * 46)
    print("1. Register New Pet")
    print("2. View All Pets")
    print("3. Search Pet")
    print("4. Edit Pet Details")
    print("5. Delete Pet")
    print("6. Add Care Record")
    print("7. View All Care Records")
    print("8. View Pet Care History")
    print("9. View Upcoming Care Activities")
    print("10. Mark Care Activity Completed")
    print("11. Delete Care Record")
    print("12. Pet Summary Report")
    print("13. Care Type Report")
    print("14. Pet-Wise Report")
    print("15. Overdue Care Report")
    print("0. Exit")
    print("=" * 46)


def main():
    initialize_storage()

    actions = {
        "1": add_pet,
        "2": view_all_pets,
        "3": search_pet,
        "4": edit_pet,
        "5": delete_pet,
        "6": add_care_record,
        "7": view_all_care_records,
        "8": view_pet_care_history,
        "9": view_upcoming_care,
        "10": complete_care_record,
        "11": delete_care_record,
        "12": pet_summary,
        "13": care_type_report,
        "14": pet_wise_report,
        "15": overdue_care_report
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Pet Care Management System!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, ValueError, KeyError, TypeError) as error:
                print(f"An error occurred: {error}")

            pause()

        else:
            print("Invalid choice. Select a number from 0 to 15.")
            pause()


if __name__ == "__main__":
    main()
