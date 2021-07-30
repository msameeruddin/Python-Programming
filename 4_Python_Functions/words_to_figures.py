import sys

Unit_List = {}
Unit_List[0] = ""
Unit_List[1] = " One"
Unit_List[2] = " Two"
Unit_List[3] = " Three"
Unit_List[4] = " Four"
Unit_List[5] = " Five"
Unit_List[6] = " Six"
Unit_List[7] = " Seven"
Unit_List[8] = " Eight"
Unit_List[9] = " Nine"

Ten_List = {}
Ten_List[0] = ""
Ten_List[10] = " Ten"
Ten_List[11] = " Eleven"
Ten_List[12] = " Twelve"
Ten_List[13] = " Thirteen"
Ten_List[14] = " Fourteen"
Ten_List[15] = " Fifteen"
Ten_List[16] = " Sixteen"
Ten_List[17] = " Seventeen"
Ten_List[18] = " Eighteen"
Ten_List[19] = " Nineteen"
Ten_List[2] = " Twenty"
Ten_List[3] = " Thirty"
Ten_List[4] = " Fourty"
Ten_List[5] = " Fifty"
Ten_List[6] = " Sixty"
Ten_List[7] = " Seventy"
Ten_List[8] = " Eighty"
Ten_List[9] = " Ninety"

Ind_Power_List = {}
Ind_Power_List[2] = " Hundred"
Ind_Power_List[3] = " Thousand"
Ind_Power_List[5] = " Lakh"
Ind_Power_List[7] = " Crore"
Ind_Power_List[9] = " Arab"
Ind_Power_List[11] = " Kharab"
Ind_Power_List[13] = " Nil"
Ind_Power_List[15] = " Padma"
Ind_Power_List[17] = " Sankha"

Int_Power_List = {}
Int_Power_List[2] = " Hundred"
Int_Power_List[3] = " Thousand"
Int_Power_List[6] = " Million"
Int_Power_List[9] = " Billion"
Int_Power_List[12] = " Trillion"
Int_Power_List[15] = " Quadrillion"
Int_Power_List[18] = " Quintillion"

def Figures_To_Words_Core(Num=0, Max_Res=100, Style="Indian"):
    """
      This function is Engine of another Function namely Figures_To_Words.
      It performs the Main logic of converting Figures into Words

      Here, it takes Minimum of One Argument, that is the Number to be converted...!

      Num expects the No. to be Converted by default it's Zero and return value is ""
      Max_Res expects the max power to be used for Quantifying No.s
        for example 1000 is One Thousand if Max_Res is 3
                and 1000 is Ten Hundred if Max_Res is 2
      Style determines the Numbering System to be used, as per updates so far, only
        two Systems are available in this function, which are
          "Indian" - implies Indian Numbering System
          "International" - implies International Numbering System

      At Last function returns the final Words_Value as a String!
    """
    k = 0
    Power_List = {}
    if Style == "Indian":
        Power_List = Ind_Power_List
    elif Style == "International" :
        Power_List = Int_Power_List
    else:
        return " Invalid Style"

    for i in Power_List:
        if 10**i > Num or Max_Res < i:
            break
        k = i

    if k == 0:
        if Num // 10 == 1:
            return Ten_List[Num]
        return Ten_List[Num // 10] + Unit_List[Num % 10]
    else:
        return Figures_To_Words_Core(Num // 10**k, Max_Res, Style) + Power_List[k] + Figures_To_Words_Core(Num % 10**k, Max_Res, Style)


def Is_Int(Num):
    try:
        x = int(Num)
        return x
    except:
        try:
            x = float(Num)
            return x // 1
        except:
            return "False"


def Resolution_Match(Max_Res):
    """
      Tries to Search the Required Resolution, in Both the Numbering Systems
      If Found, it Returns the Resolution String
      else Returns the Empty String
    """
    Res_Check = False
    if Max_Res == "":
        return 100

    if str(Max_Res).casefold() == "Hundred".casefold():
        return 2

    for Power in Ind_Power_List.keys():
        if str(Ind_Power_List[Power]).strip().casefold() == str(Max_Res).strip().casefold():
            return Power

    for Power in Int_Power_List.keys():
        if str(Int_Power_List[Power]).strip().casefold() == str(Max_Res).strip().casefold():
            return Power

    if Res_Check == False:
        print(" Invalid Resolution.., So, Assuming Max Resolution")
        return ""
    return Max_Res


def Figures_To_Words(Num=0, Max_Res="", Style="Indian"):
    """
    As Per Expectations, This functions doesn't Actually converts into Words
    but rather pre-process the input to feed into its Engine function named as Figures_To_Words_Core()
    Programmer didn't put this formatting, into the Engine function as it uses concept of Recursion
      and Programmer doesn't finds it interesting to check basic conditions in every sub-part of Function

    So, this Function Expects/Takes the following arguments
      Num - Original No. to be Converted
      Style - Determines the Numbering System to be used, it can be either "Indian" or "International" as of Now
      Max_Res - It takes Max_Res to be used while Conversion as a String, so as to convert into Power form and 
                give input to core function. If Max_Res belongs to a conflicting Styled Numbering System, 
                then the priority is given to this Argument and Style changes accordingly

      And Finally, it Returns the Actual Converted String with the Help of its Core Function
    """
    Result = ""
    if Is_Int(Num) != "False":
        if Num == 0:
            return " Zero"
        elif Num < 0:
            Result = " Minus"
            Num = -Num
    else:
        return "False"

    Style_Check = False

    for Standard in ["Indian", "International"]:
        if Standard.casefold() == str(Style).casefold():
            Style = Standard
            Style_Check = True
            break

    if Style_Check == False:
        Style = "Indian"

    if(Is_Int(Max_Res) == "False"):
        Max_Res = Resolution_Match(Max_Res)
    if Max_Res in Ind_Power_List.values():
        Style = "Indian"
    elif Max_Res in Int_Power_List.values():
        Style = "International"
    return Result + Figures_To_Words_Core(Num, Max_Res, Style)


print("   Hi, Here we have got a Number to Words Converter ...!! ")
print("     Here are the Instruction for the Input.. Please Read this Before Proceeding Further!")
print("        - To Toggle between Indian and International Numbering System..  Press 'T' in Number Input")
print("        - To get Output in Both Numbering Systems.. Press 'B' in Number Input")
print("        - To Define Max Resolution during Conversion, Enter the Resolutionary Power (Like 'Thousand', 'Million' etc)")
print("            and Enter 'Max' for Maximum Resolution")
print("           Entering Any of the Above Input, Performs the Adjustments and then results in Request of Another Input ")
print("             where, any Integer can be Entered for Evaluation")
print("        - Finally, To End the Input, Press 'Enter' without any Input \n")

N = "Hi"
Stylo = "Indian"
Reso = ""

def Toggle_Style(Silence=False):
    global Stylo
    if Stylo == "Indian":
        Stylo = "International"
    elif Stylo == "International" or Stylo == "Both":
        Stylo = "Indian"
    else:
        Stylo = "Indian"

    if Silence == False:
        print("   Toggled Successfully ..\n")



while N != "":
    N = input("  Enter a Number - ")
    if(N == ""):
        print("   Thank You!  Program Terminates.. \n")
        sys.exit()
    if Is_Int(N) != "False":
        if Stylo == "Both":
            print("    " + Figures_To_Words(Is_Int(N), Reso, "Indian"))
            print("    " + Figures_To_Words(Is_Int(N), Reso, "International") + "\n")
        else:
            print("    " + Figures_To_Words(Is_Int(N), Reso, Stylo) + "\n")
    elif N.strip().casefold() == "T".casefold():
        Toggle_Style()
    elif N.strip().casefold() == "B".casefold():
        Stylo = "Both"
        print("    Updated Successfully ..\n")
    elif N.strip().casefold() == "Max".casefold():
        Reso = 100
        print("    Updated Successfully ..\n")
    else:
        Reso = Resolution_Match(N)
        if Reso == "":
            print(" Sorry, that doesn't Corresponds to any Kind of Input... \n")
        else:
            print("    Updated Resolution Successfully... \n")

            if str(N).strip().casefold() == "Hundred".casefold():
                continue
            if str(N).strip().casefold() == "Thousand".casefold():
                continue

            for Power in Ind_Power_List.values():
                if str(N).strip().casefold() == str(Power).strip().casefold():
                    Stylo = "Indian"
                    break
           
            for Power in Int_Power_List.values():
                if str(N).strip().casefold() == str(Power).strip().casefold():
                    Stylo = "International"
                    break