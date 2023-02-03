import pyautogui
import keyboard

while True:
    x, y = pyautogui.position()
<<<<<<< HEAD
<<<<<<< HEAD
    color = pyautogui.screenshot().getpixel((200, 200))
=======
    color = pyautogui.screenshot().getpixel((960, 138))
>>>>>>> 995a8e2d154b74172387f309bef7e62affbd57ac
=======
    color = pyautogui.screenshot().getpixel((x, y))
>>>>>>> 9fc1e4e4d3d4aaaad7a59f9f43da2bdbaba323ab
    print(f'x: {x}, y: {y}, color: {color}')
    if keyboard.is_pressed('q'):
        break
