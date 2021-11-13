"""ASS5 PROG1:
 Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage.
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good"""

#Ass5 Prog1, 1st try

import sys

def AskInput():
    print()
    GradePerc = float(input("Give a grade percentage (65-100 only):  "))
    return GradePerc

def SolveGradeMark(GradePercF):
    RoundGradePercF = round(GradePercF)

    if RoundGradePercF <= 100 and RoundGradePercF >= 97:
        GradeMark = 1.0
        Description = "Excellent"
        
    elif RoundGradePercF <= 96 and RoundGradePercF >= 94:
        GradeMark = 1.25
        Description = "Excellent"

    elif RoundGradePercF <= 93 and RoundGradePercF >= 91:
        GradeMark = 1.5
        Description = "Very Good"

    elif RoundGradePercF <= 90 and RoundGradePercF >= 88:
        GradeMark = 1.75
        Description = "Very Good"

    elif RoundGradePercF <= 87 and RoundGradePercF >= 85:
        GradeMark = 2.0
        Description = "Good"

    elif RoundGradePercF <= 84 and RoundGradePercF > 82:
        GradeMark = 2.25
        Description = "Good"    
    
    elif RoundGradePercF <= 81 and RoundGradePercF >= 79:
        GradeMark = 2.5
        Description = "Satisfactory"    

    elif RoundGradePercF <= 78 and RoundGradePercF >= 76:
        GradeMark = 2.75
        Description = "Satisfactory"  

    elif RoundGradePercF == 75:
        GradeMark = 3.0
        Description = "Passing" 

    elif RoundGradePercF <= 74 and RoundGradePercF >= 65:
        GradeMark = 5.0
        Description = "Failure" 

    else:
        print()
        print("Invalid Grade Input \nThe progam is closing. Try again next time.\n  ")
        sys.exit()

    return GradeMark, Description, RoundGradePercF

def Display (GradeMark, GradePerc, Description, RoundedGradePerc):
    print()
    print (f"Grade Percentage = {GradePerc} ≈ {RoundedGradePerc}\nGrade Mark = {GradeMark} \nDescription = {Description}")
    print()

#1 Ask grade perc
FinalGradePerc = AskInput()

#2 assign equivalent mark and description
FinalGradeMark, FinalDescription, FinalRoundedGradePerc = SolveGradeMark(FinalGradePerc)

#3 display mark grade with description
Display(FinalGradeMark, FinalGradePerc, FinalDescription, FinalRoundedGradePerc)