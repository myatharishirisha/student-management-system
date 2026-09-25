# Student Management System

A menu-driven Student Management System built using Python.

## Features

* Add Student
* Display Students
* Update Student
* Delete Student
* Add Marks to Student
* Display Student Marks
* Unique Student ID validation
* Student ID not-found handling

## Subjects

The system stores marks for:

* Math
* Science
* English
* Computer
* History

## Concepts Used

* Python Functions
* Lists
* Dictionaries
* Nested Dictionaries
* Loops
* Conditional Statements
* User Input
* CRUD Operations
* Input Validation

## Student Data Structure

Each student is stored as a dictionary inside a list.

```python
{
    "Id": "1",
    "name": "Ravi",
    "age": 20,
    "course": "B.Tech",
    "marks": {
        "Math": 85,
        "Science": 78,
        "English": 90,
        "Computer": 88,
        "History": 76
    }
}
```

## Menu

```text
===== Student Management System =====
1. Add Student
2. Display Students
3. Update Student
4. Delete Student
5. Add Marks to Student
6. Exit
```

## How to Run

Make sure Python is installed.

Run the following command:

```bash
python student_management.py
```

## Purpose

This project was created to practice Python programming concepts including functions, lists, dictionaries, nested dictionaries, loops, conditions, CRUD operations, and user input handling.
