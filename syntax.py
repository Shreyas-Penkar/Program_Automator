import pyautogui
def c():
        pyautogui.write("//untitled")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("#include<stdio.h>")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("void main()")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("{")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("printf(\"hello\");")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        


def cpp():
        pyautogui.write("//untitled")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("#include<iostream>")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("using namespace std;")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("int main()")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("{")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("cout<<\"hello\"<<endl;")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("return 0;")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

def java():
        global name
        pyautogui.write("//untitled")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("import java.util.Scanner;")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        class_statement="public class Program"
        pyautogui.write(class_statement)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("{")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("public static void main(String[] args)")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("{")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("Scanner ob= new Scanner(System.in);")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.write("System.out.println(\"hello\");")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

def html():
    pyautogui.write("html")
    pyautogui.press("tab")

def css():
    print("//hello")

def js():
    print("//hello")

def py():
    print("#hello")    

def bash_script():
    pyautogui.write("#!/bin/bash")

