# Student Management System

A simple menu-driven Student Management System built with Python. It stores records locally in a JSON file, so data remains available after the program closes.

## Features
- Add a student with roll number, name, course, and marks
- View all student records
- Search by roll number
- Update student details
- Delete a student with confirmation
- Show class summary (student count, average marks, topper)
- Input validation and duplicate roll-number prevention
- Persistent storage using `students.json`

## Requirements
- Python 3.8 or newer
- No external packages required

## Run
```bash
python main.py
```

The `students.json` file is created automatically when the first student is added.

## Project structure
```text
Student-Management-System/
├── main.py
├── students.json
└── README.md
```

## Learning outcomes
Python functions, loops, conditionals, lists, dictionaries, exception handling, JSON file handling, and basic CRUD operations.
