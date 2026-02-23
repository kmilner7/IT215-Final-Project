# Student Grade Tracker

#### Video Demo: ((https://youtu.be/Wmq6kzEf7Oo))

#### Description:

Student Grade Tracker is a Python command-line application designed to help users manage and track student grades efficiently. The purpose of this project is to demonstrate core programming concepts including functions, file handling, loops, conditionals, and data structures such as lists and dictionaries.

This program allows users to add students, assign grades, and generate reports that display averages, highest grades, and lowest grades. The data is stored in a JSON file so that information is saved even after the program is closed. This ensures persistence and allows users to continue managing their grade records in future sessions.

The application runs through a menu system controlled by the main() function. Users are presented with several options including adding a student, adding a grade, viewing reports, and exiting the program. When exiting, the data is automatically saved to a file called grades.json.

Files Included in This Project:

TermProject.py:
This is the main program file. It contains the main function along with several additional functions including:
- load_data()
- save_data()
- add_student()
- add_grade()
- view_report()

Each function is designed to handle a specific task, making the program modular and easy to maintain.

requirements.txt:
This file lists any required libraries. This project only uses built-in Python libraries such as json and os, so no external installations are required.

grades.json:
This file is automatically created when the program runs. It stores student names and grades in structured JSON format.

Design Decisions:

One key design decision was to use a dictionary to store student names as keys and their grades as values in lists. This structure allows easy access to each student’s data and simplifies calculations for averages and statistics.

Another design choice was implementing separate functions for each major task instead of writing all code inside the main function. This improves readability, organization, and maintainability of the code.

Complexity and Learning Outcomes:

This project goes beyond simple lab assignments by combining file handling, structured program design, data persistence, and user interaction into one cohesive system. It demonstrates an understanding of Python programming fundamentals and real-world application development.

Future Improvements:

In the future, this project could be expanded by adding:
- A graphical user interface
- Grade letter conversions (A, B, C, etc.)
- CSV export functionality
- Data visualization charts

Overall, the Student Grade Tracker demonstrates practical problem-solving skills and structured program implementation using Python.
