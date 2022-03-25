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
# Implementation of object oriented programming---------------------------------
# i want to some how store the action in a list or something

class ActionElement:  # this is the class for every action type, like, mouse click, double click, keypress..,.. everthing.#this would hold the squence of action, macro key with which they are tied.
    squenceNumber = None
    # this is the macro key that the key action is tied to.
    macroKeyThatExecutesMe = None
    pass

class MouseSingleClick(ActionElement):
    def __init__(self, XCoordinate=None, YCoordinate=None):
        self.Xcoordinate = XCoordinate
        self.Ycoordinate = YCoordinate

    def click(self):
        XorignalCursorPosition = pyautogui.position().x #originalCursorPosition is the postition of mouse before the mouse moved to record the macro
        YorignalCursorPosition = pyautogui.position().y #originalCursorPosition is the postition of mouse before the mouse moved to record the macro
        pyautogui.click(self.Xcoordinate, self.Ycoordinate)
        pyautogui.moveTo(XorignalCursorPosition, YorignalCursorPosition)

class MouseDoubleClick(MouseSingleClick):
    # def __init__(self, XCoordinates = None, YCoordinates = None):
    #     self.Xcoordinate = XCoordinates
    #     self.Ycoordinate = YCoordinates
    def __init__(self, XCoordinate=None, YCoordinate=None):
        super().__init__(XCoordinate, YCoordinate)

    def click(self):
        XorignalCursorPosition = pyautogui.position().x #originalCursorPosition is the postition of mouse before the mouse moved to record the macro
        YorignalCursorPosition = pyautogui.position().y #originalCursorPosition is the postition of mouse before the mouse moved to record the macro
        pyautogui.doubleClick(self.Xcoordinate, self.Ycoordinate)
        pyautogui.moveTo(XorignalCursorPosition, YorignalCursorPosition)

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
            if i == singleClickActionObject:
                i.click()
        pass
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
                    singleClickActionObject = MouseSingleClick()
                    listOfActions.append(singleClickActionObject)
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    for i in range(1, input_delay+1):
                        print("tik tik", i)
                        time.sleep(1)
                    singleClickActionObject.Xcoordinate =  pyautogui.position().x
                    singleClickActionObject.Ycoordinate =  pyautogui.position().y
                    #~~~~~~~~~~~~~~~Object created and after calling click method, it should perform the click~~~~~~~~~~~~~~~~~~#
                    # print("waiting for macro key to be pressed...")
                    # keyboard.wait(inputMacroKey)
                    # singleClickActionObject.click()

                    break
                elif newMacroActionType_UserInput == 2:
                    #here goes the code for double click
                    doubleClickActionObject = MouseDoubleClick()
                    input_delay = int(input("Enter the amount of delay(in seconds) you want before positioning your mouse on the desired location:- "))
                    for i in range(1, input_delay+1):
                        print("tik tik", i)
                        time.sleep(1)
                    doubleClickActionObject.Xcoordinate =  pyautogui.position().x
                    doubleClickActionObject.Ycoordinate =  pyautogui.position().y
                    #~~~~~~~~~~~~~~~Object created and after calling click method, it should perform the click~~~~~~~~~~~~~~~~~~#
                    print("waiting for macro key to be pressed...")
                    keyboard.wait(inputMacroKey)
                    doubleClickActionObject.click()
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                    break
                elif newMacroActionType_UserInput == 3:
                    # here goes the code for keypress
                    print("Press the macro key for the action(press escape after pressing the key)")
                    inputMacroKey = keyboard.record(until='esc')
                    inputMacroKey = str(inputMacroKey[0])
                    inputMacroKey = inputMacroKey[14:-6]
                    print("Press the key you want to be pressed with the macro(press escape after pressing the key)")
                    actionKey = keyboard.record(until='esc')#its the key the user wants the program to press after he presses the macro key
                    actionKey = str(actionKey[0])
                    actionKey = actionKey[14:-6]
                    print("The key you pressed was --->", actionKey)
                    print("Your selected macro key was --->", inputMacroKey)
                    print("waiting for macro key to be pressed...")
                    keyboard.wait(inputMacroKey)
                    pyautogui.press(actionKey)
                    print("Action executed successfully")
                break
    else:#for an invalid input
        print("\nInvalid input try again!\n")
        userChoiceToMakeNewMacrosOrUseExisting = int(input("Enter the number corresponding to the choice: \n0. Exit\n1. Use your created shortcuts\n2. Create new macros\nYour Input ---> "))