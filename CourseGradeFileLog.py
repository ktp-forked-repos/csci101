#!/usr/bin/python2
# CourseGradeiFileLog.py
# https://csintro.mines.edu/csci101/wiki/PythonAssignments/CourseGradeFileLog

fileName = raw_input("Enter a filename: ")
studentsName = raw_input("Enter the student's name: ")
medianGroupScore = input("Enter the median group score on quizzes: ")
individualQuizScore = input("Enter the individual quiz score: ")
assignmentScore = input("Enter the assignment score: ")
firstExamScore = input("Enter the first exam score: ")
secondExamScore = input("Enter the second exam score: ")
finalExamScore = input("Enter the final exam score: ")

courseGrade = (medianGroupScore * 0.12 +
               individualQuizScore * 0.12 +
               assignmentScore * 0.16 +
               firstExamScore * 0.15 +
               secondExamScore * 0.20 +
               finalExamScore * 0.25)

fileLog = file(fileName, "a")

fileLog.write("%s %.2f %.2f %.2f %.2f %.2f %.2f %.2f\n" % (
              studentsName,
              courseGrade,
              finalExamScore,
              firstExamScore,
              secondExamScore,
              assignmentScore,
              individualQuizScore,
              medianGroupScore)
            )
fileLog.close()
