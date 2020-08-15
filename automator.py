import pyautogui
import subprocess
import os
from syntax import *


name=""
extension=["c","cpp","java","html","css","js","py","sh","bat"]


def complex_key_presser(str1, str2):
    pyautogui.keyDown(str1)
    pyautogui.keyDown(str2)

    pyautogui.PAUSE = 0.2

    pyautogui.keyUp(str2)
    pyautogui.keyUp(str1)


    

def save():
    global name
    for i in range(0, 6):
              pyautogui.press('ctrl')
    complex_key_presser('ctrl', 's')

    for i in range(0, 6):
              pyautogui.press('tab')

    pyautogui.press('enter')
        
    pyautogui.write("C:\\Users\\suhas\\Desktop\\GITHUB\\Program_Automator")      #change
 
    pyautogui.press('enter')

    for i in range(0, 6):
              pyautogui.press('tab')
    

    pyautogui.write(name)      

    pyautogui.press('enter')  



def main():
    # selector()
    
    global name
    global extension

    while True:
        os.system("cls")

        print()
        print("===================")
        print("|PROGRAM AUTOMATOR|")
        print("===================     - Br4v3_H3r0")
        print()

    
        print("CHOOSE YOUR OPTION")
        print("==================")
        print()
        print("1) C prog\n")
        print("2) C++ prog\n")
        print("3) Java prog\n")
        print("4) HTML prog\n")
        print("5) CSS prog\n")
        print("6) JavaScript prog\n")
        print("7) Python prog\n")
        print("8) bash Script\n")
        print("9) Batch Script\n")
        print("q) Quit\n")
        print()
        chosen_option = input(">>> ")
        print()

        if chosen_option=='1' or chosen_option=='2' or chosen_option=='3' or chosen_option=='4' or chosen_option=='5' or chosen_option=='6' or chosen_option=='7' or chosen_option=='8' or chosen_option=='9' or chosen_option=='q' or chosen_option=='Q':
            break
    pass        

    if chosen_option=='q' or chosen_option=='Q':
        print("")
        print("SEE YA LATER H4CKER :)")
        exit()

    print("enter file name\n")
    name=input(">>> ")

     
    # os.chdir(r"cd C:\\Program Files\\Sublime Text 3")
    # os.system("subl.exe")
    
    subprocess.call([r'open.bat'])
    
    for i in range(0, 6):
        pyautogui.press('ctrl')
    complex_key_presser('ctrl', 'n')

    for i in range(0, 5):
        pyautogui.press('ctrl')

    if chosen_option == '1':
       c() 
    elif chosen_option == '2':
       cpp() 
    elif chosen_option == '3':
       java()
    elif chosen_option == '4':
       name=name+"."+extension[int(chosen_option)-1]
       save() 
       html()
    elif chosen_option == '5':
       css()
    elif chosen_option == '6':
       js()
    elif chosen_option == '7':
       py()  
    elif chosen_option=='8':
       bash_script()



    if chosen_option!='4' or chosen_option!='q' or chosen_option!='Q':
       name=name+"."+extension[int(chosen_option)-1]
       save()
        

        


main()
