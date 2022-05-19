# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:33:29 2022

@author: Nguyen

This module provide function(s) as grading service(s)
"""

import pandas as pd

def gradeStudents(students):
    """
    Grade all students in a class and show statistic of that class

    Parameters
    ----------
    students : List of students, each student is a list contains ID and answers

    Returns
    -------
    Dataframe contains 2 columns: StudentID and Total (grade)

    """
    
    answerKey = "BADDCBDACCDBABACBDACAABDD"
    columns = ["StudentID", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
               "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21",
               "A22", "A23", "A24", "A25"]
    df = pd.DataFrame(data = students, columns = columns)
    
    # Delete columns[0] (StudentID) so from now columns is from A1 -> A25
    del columns[0]
    
    # Compare student answer with answerKey and give grade
    for i in range(25):
        df.loc[df[columns[i]] == "", columns[i]] = 0
        df.loc[df[columns[i]] == answerKey[i], columns[i]] = 4
        df.loc[(df[columns[i]] != 0) & (df[columns[i]] != 4), columns[i]] = -1
        
    # Create total grade column and change to type int16
    df["Total"] = df.loc[:,"A1":"A25"].sum(axis = 1)
    df["Total"] = df["Total"].astype("int16")
    
    # Show statistic in class
    print("********** Statistic **********")
    highScore = df.loc[df["Total"] > 80, "Total"].count()
    print("Total student with high score: " + str(highScore))
    mean = round(df["Total"].mean(), 3)
    print("Mean (average) score: " + str(mean))
    maxScore = df["Total"].max()
    print("Highest score: " + str(maxScore))
    minScore = df["Total"].min()
    print("Lowest score: " + str(minScore))
    print("Range of scores: " + str(maxScore - minScore))
    median = round(df["Total"].median(), 3)
    print("Median score: " + str(median))
    
    # Count how many wrong/skip answer for all question
    wrongAnswersCount = []
    skipAnswersCount = []
    for column in columns:
        values = df[column].value_counts()
        wrongAnswersCount.append(values[-1] if (-1) in values else 0)
        skipAnswersCount.append(values[0] if 0 in values else 0)
    maxWrongCount = max(wrongAnswersCount)
    maxSkipCount = max(skipAnswersCount)
    
    totalStudents = len(df)
    wrongRate = round(maxWrongCount / totalStudents, 3)
    skipRate = round(maxSkipCount / totalStudents, 3)
    
    # Get the question that most student answer wrong/skip
    mostWrongAnswers = []
    mostSkipAnswers = []
    for i in range(25):
        if wrongAnswersCount[i] == maxWrongCount:
            mostWrongAnswers.append(str(i + 1) + " - " + str(maxWrongCount) + " - "
                                    + str(wrongRate))
        if skipAnswersCount[i] == maxSkipCount:
            mostSkipAnswers.append(str(i + 1) + " - " + str(maxSkipCount) + " - "
                                   +str(skipRate))
    print("Question that most student skip: " + ", ".join(mostSkipAnswers))
    print("Question most student answer incorrectly: " + ", ".join(mostWrongAnswers) + "\n")
    
    return df[["StudentID", "Total"]]
