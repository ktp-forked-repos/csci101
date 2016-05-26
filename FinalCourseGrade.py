#!/usr/bin/python2
# Copied from CourseGrade.py
# https://csintro.mines.edu/csci101/wiki/PythonAssignments/CourseGrade

medianGroupScore = 90
individualQuizScore = 98.1
assignmentScore = 100
firstExamScore = 92.8
secondExamScore = 100

def classGrade(finalExamScore):
   return (medianGroupScore * 0.12 +
           individualQuizScore * 0.12 +
           assignmentScore * 0.16 +
           firstExamScore * 0.15 +
           secondExamScore * 0.20 +
           finalExamScore * 0.25)

print "Final exam:        Clas Grade:"
print 0, "                ", classGrade(0)
print 10, "               ", classGrade(10)
print 20, "               ", classGrade(20)
print 30, "               ", classGrade(30)
print 31, "               ", classGrade(31)
print 40, "               ", classGrade(40)
print 50, "               ", classGrade(50)
print 60, "               ", classGrade(60)
print 70, "               ", classGrade(70)
print 71, "               ", classGrade(71)
print 80, "               ", classGrade(80)
print 90, "               ", classGrade(90)
print 95, "               ", classGrade(95)
print 100, "              ", classGrade(100)
