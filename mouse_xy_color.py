import pyautogui
import keyboard

while True:
    x, y = pyautogui.position()
<<<<<<< HEAD
    color = pyautogui.screenshot().getpixel((200, 200))
=======
    color = pyautogui.screenshot().getpixel((960, 138))
>>>>>>> 995a8e2d154b74172387f309bef7e62affbd57ac
    print(f'x: {x}, y: {y}, color: {color}')
    if keyboard.is_pressed('q'):
        break
