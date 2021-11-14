"""ASS5 PROG3:
Program 3: Life stages
Create a program that ask for an age of a person
Display the life stage of the person.
Rules:
0 - 12 : Kid
13 - 17 : Teen
18 : Debut
19 above : Adult"""

#Ass5 Prog3, 1st try,   

import sys

def AskAge():
    Age = int(input("\nTell me your age & I'll tell your life stage.\nHow old are you?  "))
    return Age 

def Check(AgeF):
    if AgeF < 0 or AgeF > 120:
        print("\nAge is INVALID!!\n \nType '1' to try again.\nType '2' to exit.")
        OneOrTwo = input("Reply:    ")
        print()
        return OneOrTwo

def Solve(AgeF):
    if AgeF >= 0 and AgeF <= 12:
        LifeStage = "KID"
    
    elif AgeF >= 13 and AgeF <= 17:
        LifeStage = "TEEN"
    
    elif AgeF == 18:
        LifeStage = "DEBUT"
    
    else:
        LifeStage = "ADULT"

    return LifeStage   

def Display(LifeStageF, AgeF):
    print()
    print(f"You are {AgeF} years old and your life stage is {LifeStageF}.\n")


#1 ask age
FinalAge = AskAge()

#2 check if valid age
FinalOneOrTwo = Check(FinalAge)

while FinalOneOrTwo == "1":
    print("Try again!")
    FinalAge = AskAge()
    FinalOneOrTwo = Check(FinalAge)

if FinalOneOrTwo == "2":
    print("Thank you for tryin!\n")
    sys.exit()

elif FinalOneOrTwo is None:
    pass

else:
    print("Please follow instruction. The program is closing. Restart to try again.\n")
    sys.exit()

#3 equivalent life stage
FinalLifeStage = Solve(FinalAge)

#4 display life stage
Display(FinalLifeStage, FinalAge)
