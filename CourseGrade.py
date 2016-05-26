#!/usr/bin/python2
# CourseGrade.py
# https://csintro.mines.edu/csci101/wiki/PythonAssignments/CourseGrade

studentsName = raw_input("Enter the student's name: ")
medianGroupScore = input("Enter the median group score on quizzes: ")
individualQuizScore = input("Enter the individual quiz score: ")
assignmentScore = input("Enter the assignment score: ")
firstExamScore = input("Enter the first exam score: ")
secondExamScore = input("Enter the second exam score: ")
finalExamScore = input("Enter the final exam score: ")

print "Student's name:", studentsName
print "Student's course grade:", (medianGroupScore * 0.12 +
                                  individualQuizScore * 0.12 +
                                  assignmentScore * 0.16 +
                                  firstExamScore * 0.15 +
                                  secondExamScore * 0.20 +
                                  finalExamScore * 0.25)
