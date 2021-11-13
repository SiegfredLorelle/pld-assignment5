"""ASS5 PROG2:
Program 2: Find the lowest number
Create a program that ask 3 numbers. 
Find the lowest number using only if-else statement.
Display the lowest number"""

#Ass5 Prog2, 1st try, 

def AskInput():
    print("\nLet me guess the lowest among 3 numbers.\n ")
    FirstNum =int(input("1st input:  "))
    SecNum = int(input("2nd input:  "))
    ThirdNum = int(input("3rd input:  "))
    return FirstNum, SecNum, ThirdNum
       
def Solve(FirstNumF, SecNumF, ThirdNumF):
   
    if FirstNumF < SecNumF and FirstNumF < ThirdNumF:
        LowestNum = FirstNumF
  
    elif SecNumF < FirstNumF and SecNumF < ThirdNumF:
        LowestNum = SecNumF

    elif ThirdNumF < FirstNumF and ThirdNumF < SecNumF:
        LowestNum = ThirdNumF

    return LowestNum
 
def Display(LowestNumF):
    print(f"\n{LowestNumF} is the lowest number.\n")

#1 ask the 3 numbers
Final1stNum, Final2ndNum, Final3rdNum = AskInput()

#2 use if-else statements to find the lowest
FinalLowestNum = Solve(Final1stNum, Final2ndNum, Final3rdNum)

#3 display the lowest number
Display(FinalLowestNum)