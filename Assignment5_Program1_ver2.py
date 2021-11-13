"""ASS5 PROG1:
 Program 1: PUP Grading System
# Section 8 of https://www.pup.edu.ph/studentservices/files/ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage.
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good"""

#Ass5 Prog1, 1st try,   using roundfunc (baka mamali kapag .5 ang deci ng input)
#            2nd try,   changed roundfunc - since hindi round up lagi pag 0.5 (rounding to nearest even number sya kapag 0.5 sa roundfunc)
#                       added input check with tryagain/exit option if invalid input                                       

import sys, math

def AskInput():
    print()
    GradePerc = float(input("Give a grade percentage (65-100 only):  "))
    return GradePerc

def Rounding(GradePercF):
    RoundGradePercF = GradePercF - math.floor(GradePercF)
    if RoundGradePercF < 0.5:
        RoundGradePercF = math.floor(GradePercF)
    elif RoundGradePercF >= 0.5:
        RoundGradePercF = math.ceil(GradePercF)
    return RoundGradePercF

def Checking(RoundGradePercF):
    if RoundGradePercF < 65 or RoundGradePercF > 100:
        print()
        print("INVALID GRADE INPUT\n \nType '1' to try again.\nType '2' to exit. ")
        OneOrTwo = input("Reply:     ")
        return OneOrTwo
    
def SolveGradeMark(RoundGradePercF):
    
    if RoundGradePercF <= 100 and RoundGradePercF >= 97:
        GradeMark = "1.0"
        Description = "Excellent"
        
    elif RoundGradePercF <= 96 and RoundGradePercF >= 94:
        GradeMark = "1.25"
        Description = "Excellent"

    elif RoundGradePercF <=93 and RoundGradePercF >= 91:
        GradeMark = "1.5"
        Description = "Very Good"

    elif RoundGradePercF <= 90 and RoundGradePercF >= 88:
        GradeMark = "1.75"
        Description = "Very Good"

    elif RoundGradePercF <= 87 and RoundGradePercF >= 85:
        GradeMark = "2.0"
        Description = "Good"

    elif RoundGradePercF <= 84 and RoundGradePercF >= 82:
        GradeMark = "2.25"
        Description = "Good"    
    
    elif RoundGradePercF <= 81 and RoundGradePercF >= 79:
        GradeMark = "2.5"
        Description = "Satisfactory"    

    elif RoundGradePercF <= 78 and RoundGradePercF >= 76:
        GradeMark = "2.75"
        Description = "Satisfactory"  

    elif RoundGradePercF == 75:
        GradeMark = "3.0"
        Description = "Passing" 

    elif RoundGradePercF <= 74 and RoundGradePercF >= 65:
        GradeMark = "5.0"
        Description = "Failure" 

    return GradeMark, Description

def Display (GradeMark, GradePerc, Description, RoundedGradePerc):
    print()
    print (f"Grade Percentage = {GradePerc} ≈ {RoundedGradePerc}\nGrade Mark = {GradeMark} \nDescription = {Description}")
    print()


#1 Ask grade perc
FinalGradePerc = AskInput()

# round grade perc
FinalRoundedGradePerc = Rounding(FinalGradePerc)

#3 check validity, ask if try again or exit
OneOrTwo = Checking(FinalRoundedGradePerc)
 
while OneOrTwo == "1":
    print("\nGive it another shot!")
    FinalGradePerc = AskInput()
    FinalRoundedGradePerc = Rounding(FinalGradePerc)
    OneOrTwo = Checking(FinalRoundedGradePerc)
    
if OneOrTwo == "2":
    print("\nThe program is closing. Thank you for trying!\n ")
    sys.exit()

elif OneOrTwo is None:
    pass

else:
    print(" \nNext time follow instructions. The program is closing. Restart if you want to try again.\n ")
    sys.exit()

#4 assign equivalent mark and description
FinalGradeMark, FinalDescription = SolveGradeMark(FinalRoundedGradePerc)

#5 display mark grade with description
Display(FinalGradeMark, FinalGradePerc, FinalDescription, FinalRoundedGradePerc)