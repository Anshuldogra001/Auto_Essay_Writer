# to use change the word name as it is in your system
# To change the size just change no. of down and up in given code at specified positions.

import pyautogui
import time
import colorama
colorama.init()
from colorama import Fore, Style
import wikipedia


def delay(x):
    time.sleep(x)


def res(search_query):

    try:
        # search_query = "Swami Vivekananda"
        page = wikipedia.page(search_query)
        introduction = page.summary

        # introduction = page.content

        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "Wait while the work is done.")

        pyautogui.press('win')
        delay(5)
        pyautogui.typewrite('Microsoft Word 2010')
        delay(5)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        time.sleep(2)
        cursor_x = 200
        cursor_y = 200
        pyautogui.moveTo(cursor_x, cursor_y)
        delay(3)

        # Type the text and format it
        pyautogui.typewrite(search_query)
        pyautogui.hotkey('ctrl', 'a')  # Select all text
        pyautogui.hotkey('ctrl', 'b')  # bold
        pyautogui.hotkey('ctrl', 'u')  # underline
        pyautogui.hotkey('ctrl', 'e')  # centre text
        pyautogui.hotkey('ctrl', 'shift','a') # all caps
        pyautogui.hotkey('ctrl', 'shift', 'f')  # Open font formatting dialog
        delay(3)

        # Change the text size current set to 36
        pyautogui.press(['tab','tab', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down'])  # Move to the size dropdown
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')  # Open the size dropdown
        delay(2)
        pyautogui.hotkey('ctrl', 'shift', 'end')
        delay(3)

        pyautogui.press('enter')
        pyautogui.press('enter')
        delay(3)

        pyautogui.hotkey('ctrl', 'b')  # bold
        pyautogui.hotkey('ctrl', 'u')  # underline
        pyautogui.hotkey('ctrl', 'l')  # left text
        pyautogui.hotkey('ctrl', 'shift','a') # all caps
        pyautogui.hotkey('ctrl', 'shift', 'f')  # Open font formatting dialog
        delay(3)

        # Change the text size current set to 36
        pyautogui.press(['tab','tab', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up'])  # Move to the size dropdown
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')  # Open the size dropdown
        delay(2)


        pyautogui.typewrite(introduction)
        pyautogui.hotkey('ctrl', 's')

        #to save store
        # time.sleep(1)
        # pyautogui.hotkey('alt', 'f4')

        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "Created he file asked! work is done.")
    except:
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "Some error occurred please try again.")\



max_len = 20
print(Fore.RED + "If want to stop type quit!!!!!")
while True:

    print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    inp = input()
    if inp.lower() == "quit":
        break

    res(inp.lower())
