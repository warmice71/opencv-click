import pyautogui
from time import sleep

sleep(10)
button7location = pyautogui.locateOnScreen('verify.png', confidence=0.6)
button7point = pyautogui.center(button7location)
button7x, button7y = button7point
pyautogui.click(button7x, button7y)