#Notes From Deep
# We need to save the macros, so that a user doesnt need to create a new macro every single time.
################
#Notes From Zaid
################

#cli of oneClickSolution
#imports------------------------------
import time
import pyautogui
import keyboard
#end of imports-----------------------
print("Welcome to OCS. Here, you can map a macro to click a button(and more!)")
userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
while True:
    if userChoiceToMakeNewMacrosOrUseExisting == 0:
        exit()
    elif userChoiceToMakeNewMacrosOrUseExisting == 1:
        print("\nwe are working on this bit...\n")
        userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
    elif userChoiceToMakeNewMacrosOrUseExisting == 2:
        while userChoiceToMakeNewMacrosOrUseExisting != 0:
            newMacroActionType_UserInput = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Mouse Single Click\n2. Mouse Double Click\n3. Key press\nYour Input ---> "))
            while newMacroActionType_UserInput != 0:
                if newMacroActionType_UserInput == 1:
                    XorignalCursorPosition = pyautogui.position().x #originalCursorPosition is the postition of mouse before the mouse moved to record the macro
                    YorignalCursorPosition = pyautogui.position().y #originalCursorPosition is the postition of mouse before the mouse moved to record the macro
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    time.sleep(input_delay)
                    pyautogui.position()
                    XpositionOfCursor = pyautogui.position().x
                    YpositionOfCursor = pyautogui.position().y
                    print("coordinates of mouse cursor --->",XpositionOfCursor, YpositionOfCursor)
                    print("press the key to which you want to map the action and then press the escape key:")
                    inputMacroKey = keyboard.record(until='esc')
                    inputMacroKey = str(inputMacroKey[0])
                    inputMacroKey = inputMacroKey[14:-6]
                    print("Your selected macro key was --->", inputMacroKey)
                    print("waiting for macro key to be pressed...")
                    keyboard.wait(inputMacroKey)
                    pyautogui.click(XpositionOfCursor, YpositionOfCursor)
                    pyautogui.moveTo(XorignalCursorPosition, YorignalCursorPosition)
                    print("Action executed successfully")
                elif newMacroActionType_UserInput == 2:
                    #here goes the code for double click
                    pass
                elif newMacroActionType_UserInput == 3:
                    #here goes the code for keypress
                    pass
            break
    else:
        print("\nInvalid input try again!\n")
        userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))