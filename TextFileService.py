# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:17:28 2022

@author: Nguyen

This module provide function(s) as service(s) to work with text file
"""

import re

def readStudentsFromFile(fileName):
    """
    Read students from text file and get valid data, inform invalid data (not get)

    Parameters
    ----------
    fileName : Name of file from user input

    Returns
    -------
    students : List of students, each student is a list contains ID and answers

    """
    
    filePath = "./Data Files/"
    fileType = ".txt"
    regEx = "^N\d{8}"
    students = []
    lineNumber = 0
    
    # Read file, validate data then save to students
    with open(filePath + fileName + fileType, "r") as reader:
        print("********** Analyzing " + fileName + " **********\n")
        for line in reader:
            lineNumber += 1
            student = line.strip().split(",")
            if len(student) != 26:
                print("Invalid data at line " + str(lineNumber) + ": expect 26 fields")
                print(line)
                continue
            if not re.match(regEx, student[0]):
                print("Invalid student ID at line " + str(lineNumber)
                      + ": expect N and 8 digits (N12345678)")
                print(line)
                continue
            students.append(student)
    
    # Show report
    if len(students) == lineNumber:
        print("No error found !\n")
    print("********** Report of " + fileName + " **********")
    print("Valid lines: " + str(len(students)))
    print("Invalid lines: " + str(lineNumber - len(students)) + "\n")
    
    return students


def writeGradedStudents(gradedStudents, fileName):
    """
    Write student IDs and their total grade to file

    Parameters
    ----------
    gradedStudents : Dataframe contains 2 columns: StudentID and Total (grade)
    fileName : Name of file from user input

    Returns
    -------
    None.

    """
    
    filePath = "./Graded/"
    fileType = "_grades.txt"
    gradedStudents.to_csv(filePath + fileName + fileType, sep = ",", header = False,
                          index = False, mode = "w")
    print("Successfully write file: " + filePath + fileName + fileType + "\n")
