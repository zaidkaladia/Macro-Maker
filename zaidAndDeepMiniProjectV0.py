# Notes From Deep
# We need to save the macros, so that a user doesnt need to create a new macro every single time.
################
# Notes From Zaid
################

# cli of oneClickSolution
# imports------------------------------
from platform import python_branch
import time
import pyautogui
import keyboard
# end of imports-----------------------
# i want to some how store the action in a list or something

# -------------------initializations-----------------------------------------------------------
listOfActions = []
# ------------------------------------------------------------------------------
print("Welcome to OCS. Here, you can map a macro to click a button(and more!)")
# choices to make new macro or make a new one.
userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
while userChoiceToMakeNewMacrosOrUseExisting != 0:
    if userChoiceToMakeNewMacrosOrUseExisting == 0:  # 0 to exit
        exit()
    elif userChoiceToMakeNewMacrosOrUseExisting == 1:  # 1 to use already created shortcuts
        # print("\nwe are working on this bit...\n")
        print("waiting for the macro key to be pressed...")
        keyboard.wait(inputMacroKey)
        for i in listOfActions:
            if i[0] == "MouseSingleClick":
                pyautogui.click(i[1], i[2])
            elif i[0] == "MouseDoubleClick":
                pyautogui.doubleClick(i[1], i[2])
            elif i[0] == "Keypress":
                keyboard.press(i[1])
    elif userChoiceToMakeNewMacrosOrUseExisting == 2:  # 2 to create new macros
        print("press the key to which you want to map the action and then press the escape key:")
        inputMacroKey = keyboard.record(until='esc')
        inputMacroKey = str(inputMacroKey[0])
        inputMacroKey = inputMacroKey[14:-6]
        print("Your selected macro key was --->", inputMacroKey)
        while True:  # asking the user what action he/she wants to execute. 0 to exit
            newMacroActionType_UserInput = int(input(
                "Enter the number corresponding to the choice: \n0. Go Back\n1. Mouse Single Click\n2. Mouse Double Click\n3. Key press\nYour Input ---> "))
            if newMacroActionType_UserInput == 0:
                userChoiceToMakeNewMacrosOrUseExisting = int(input(
                    "\nYou got back\n\nEnter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))
                break
            while newMacroActionType_UserInput != 0:
                if newMacroActionType_UserInput == 1:  # choice for single click
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    for i in range(1, input_delay+1):
                        print("tik tik", i)
                        time.sleep(1)
                    listForMouseSingleClick = ["MouseSingleClick", pyautogui.position().x, pyautogui.position().y]
                    listOfActions.append(listForMouseSingleClick)
                    break
                elif newMacroActionType_UserInput == 2:# Choice For Double Click
                    #here goes the code for double click
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    for i in range(1, input_delay+1):
                        print("tik tik", i)
                        time.sleep(1)
                    listForMouseDoubleClick = ["MouseDoubleClick", pyautogui.position().x, pyautogui.position().y]
                    listOfActions.append(listForMouseDoubleClick)
                    break
                elif newMacroActionType_UserInput == 3:
                    print("Press the key you want to be pressed with the macro(press escape after pressing the key)")
                    time.sleep(1)
                    actionKey = keyboard.record(until='esc')#its the key the user wants the program to press after he presses the macro key
                    actionKey = str(actionKey[0])
                    print(actionKey)
                    actionKey = actionKey[14:-6]
                    print("The key you pressed was --->", actionKey)
                    listForKeypresses = ["Keypress", actionKey]
                    listOfActions.append(listForKeypresses)
                break
    else:#for an invalid input
        print("\nInvalid input try again!\n")
        userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))