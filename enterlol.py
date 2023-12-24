#dois clicks no lol
import pyautogui
import time

#area de trab
pyautogui.hotkey('win', 'm')
pyautogui.sleep(2)

#click
pyautogui.press('win') # pressiona a tecla do Windows
pyautogui.write('League of Legends') # digita o nome do LoL
pyautogui.sleep(2)
pyautogui.press('enter') # pressiona a tecla Enter para abrir o LoL

