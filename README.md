# Pet Care Management System

A simple, menu-driven Python application for managing pet information and maintaining pet care records. It helps pet owners organize feeding, vaccinations, grooming, medication, and medical visits.

## Features

- Register multiple pets
- Store pet name, type, breed, age, and owner details
- Search, edit, and delete pet records
- Add feeding and vaccination records
- Track grooming and medical appointments
- Record activity dates and next due dates
- Maintain individual pet care histories
- View upcoming care activities
- Mark care activities as completed
- Identify overdue care activities
- Generate pet-wise and care-type reports
- Store data in JSON files

## Technologies Used

- Python 3
- JSON
- datetime
- collections

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Pet-Care-Management-System.git
```

### 2. Open the project directory

```bash
cd Pet-Care-Management-System
```

### 3. Run the application

```bash
python main.py
```

No external packages are required.

## Project Structure

```text
Pet-Care-Management-System/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── pet_manager.py
├── care_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    ├── pets.json
    └── care_records.json
```

## How to Use

1. Register a pet and note its generated Pet ID.
2. Add care records using that Pet ID.
3. Select the care activity type.
4. Enter the activity date and optional next due date.
5. View upcoming and overdue care activities.
6. Mark activities completed after they are performed.
7. Generate pet-wise and care-type reports.

## Data Storage

The application uses two JSON files:

- `pets.json` stores pet information.
- `care_records.json` stores care activities and their schedules.

Pet care history is retained when a pet profile is deleted.

## Learning Outcomes

- Python functions and modules
- JSON file handling
- Lists and dictionaries
- Date validation and comparisons
- Searching and filtering records
- Collections and report generation
- Menu-driven application development

## Future Improvements

- Add a graphical user interface
- Integrate SQLite or MySQL
- Add automated vaccination reminders
- Export pet records to PDF
- Add pet photographs
- Add multiple user accounts

## Author

Python Project Challenge 

## License

Free to use for educational and personal learning purposes.
