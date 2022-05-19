# Project-Test-Grade-Calculator
This project is an assignment of Data science course

## How to run application:

### Prepare environment:

1. Clone this repositiory
2. Use an IDE which can run Python 3 to run file nguyen_nguyen_grade_the_exams.py

### Application rules:

* Enter a class name to grade, or enter "e"/"E" to exit application
* App will inform if you give wrong class name and return to menu
* App will read students of a class from file, validate data and show report
* Then application will auto grade student, show statistic of class and save graded students to file

## Development:

* Main module nguyen_nguyen_grade_the_exams.py run app and handle exception
* Module TextFileService.py provide functions to get students from file and save graded students to file
* Module GradingService.py provide function to auto grade students
* Folder `Data Files` contains files of classes, which contain student IDs and their answers
* Application read data from files in `Data Files` folder
* Folder `Graded` contains files of classes, which contains student IDs and their total grades
* Application write files save in `Greaded` folder

## GitHub link:
[Nguyen Nguyen](https://github.com/nguyennguyen0110/Project-Test-Grade-Calculator)
