"""ASS5 PROG2:
Program 2: Find the lowest number
Create a program that ask 3 numbers. 
Find the lowest number using only if-else statement.
Display the lowest number"""

#Ass5 Prog2, 1st try,   baka mag error if same inputs (error kapag ung lowest ay 2x or more ininput)
#            2nd try,   allowed same inputs, added decimals, added input number in display
#            3rd try,   changed some wording, used else instead of another if

def AskInput():
    print("\nGive me 3 NUMBERS & let me guess the lowest among 3.\n ")
    FirstNum = float(input("1st input/number:  "))
    SecNum = float(input("2nd input/number:  "))
    ThirdNum = float(input("3rd input/number:  "))
    return FirstNum, SecNum, ThirdNum
       
def Solve(FirstNumF, SecNumF, ThirdNumF):
    # incase equal lahat
    if ThirdNumF == FirstNumF == SecNumF:     
        LowestNum = ThirdNumF
        InputNum = "1st, 2nd, & 3rd input"

   # incase equal dalawa
    elif FirstNumF == SecNumF or FirstNumF == ThirdNumF or SecNumF == ThirdNumF:             

        if FirstNumF == SecNumF:
            if FirstNumF < ThirdNumF:
                LowestNum = FirstNumF
                InputNum = "1st & 2nd input"
            else:
                LowestNum = ThirdNumF
                InputNum = "3rd input"

        elif FirstNumF == ThirdNumF:
            if FirstNumF < SecNumF:
                LowestNum = FirstNumF   
                InputNum = "1st & 3rd input"    
            else:
                LowestNum = SecNumF
                InputNum = "2nd input"

        elif ThirdNumF == SecNumF:
            if ThirdNumF < FirstNumF:
                InputNum = "2nd & 3rd input"
                LowestNum = ThirdNumF
            else:
                LowestNum = FirstNumF
                InputNum = "1st input"

    #pag walang equal
    elif FirstNumF < SecNumF and FirstNumF < ThirdNumF:
        LowestNum = FirstNumF
        InputNum = "1st input"
  
    elif SecNumF < FirstNumF and SecNumF < ThirdNumF:
        LowestNum = SecNumF
        InputNum = "2nd input"

    else:
        LowestNum = ThirdNumF
        InputNum = "3rd input"

    return LowestNum, InputNum
 
def Display(LowestNumF, InputNumF):
    if (LowestNumF - int(LowestNumF)) == 0:   #para lng d lumabas ung .0 kapag integer nmn ung initial input
        LowestNumF = int(LowestNumF) 
    print(f"\n{LowestNumF} is the lowest number.\nIt was the {InputNumF}.\n")

#1 ask the 3 numbers
Final1stNum, Final2ndNum, Final3rdNum = AskInput()

#2 use if-else statements to find the lowest
FinalLowestNum, FinalInputNum = Solve(Final1stNum, Final2ndNum, Final3rdNum)

#3 display the lowest number
Display(FinalLowestNum, FinalInputNum)