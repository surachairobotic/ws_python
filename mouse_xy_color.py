import pyautogui
import keyboard

while True:
    x, y = pyautogui.position()
    color = pyautogui.screenshot().getpixel((x, y))
    print(f'x: {x}, y: {y}, color: {color}')
    if keyboard.is_pressed('q'):
        break
