# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:46:11 2022

@author: Nguyen

MAIN MODULE
This module run an application that give grade to all students in a class.
Enter a class name to give grade, you have to re-enter if gave a wrong class name.
Enter "e" to exit application.
Graded class will be save in folder "Graded" as a text file.
"""

from TextFileService import readStudentsFromFile
from TextFileService import writeGradedStudents
from GradingService import gradeStudents

appRunning = True
while(appRunning):
    
    # Show menu
    print("\n\t******************** MENU ********************")
    print("\t-- Enter class name to grade (class1 - class8)")
    print("\t-- Enter \"e\" to exit")
    answer = input("\tYour choice: ")
    print()
    
    # Exit if enter "e" or "E"
    if "e" == answer.lower():
        appRunning = False
        print("Exiting program ...")
        continue
    
    # Try to read students from file, give grade, then save graded students to file
    try:
        students = readStudentsFromFile(answer)
        if not students:
            raise Exception("File is empty")
        gradedStudents = gradeStudents(students)
        writeGradedStudents(gradedStudents, answer)
    
    # Inform if file not found and return to menu where user can re-enter class name
    except FileNotFoundError:
        print("Class name \"" + answer + "\" not found\n")
        continue
    
    # Show other error (if any) and exit application
    except Exception as e:
        print(str(e))
        appRunning = False
        print("Exiting program ...")
        continue

print("********** Program ended **********")
