import pyautogui
import random
import time

count = 0
# give yourself time to switch to the correct window
time.sleep(5)

# open the text file and read its contents
with open("keys.txt", "r") as f:
    code = f.read()

# simulate the keystrokes for each line of code
for line in code.split("\n"):
    # simulate a SHIFT+TAB key press to move to the beginning of the line
    pyautogui.press("home")
    # type the line character by character with random delays between keystrokes
    for char in line:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.02, 0.04)) #0.05, 0.15
    # simulate an ENTER key press with random delays before and after
    time.sleep(random.uniform(0.1, 0.4)) #0.5-0.7
    pyautogui.press("enter")
    time.sleep(random.uniform(0.1, 0.4)) #0.5-0.7
    
    # Extra "Enter" press to prevent auto-complete from IDE
    #In this case in the first 5 lines insert an extra "Enter"
    count += 1
    if(count < 5):
        pyautogui.press("enter")