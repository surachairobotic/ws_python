import pyautogui, time, keyboard
from PIL import ImageGrab

class Mouse():
    def delay(self, t):
        time.sleep(t)
    def btn_status(self, x, y):
        screen = ImageGrab.grab()
        color = screen.getpixel((x, y))
        return color
    def move(self, x, y):
        pyautogui.moveTo(x, y, duration=2.0)
    def click(self, x, y):
        pyautogui.moveTo(x, y, duration=1.0)
        pyautogui.leftClick()
    def clickVibrationMeasurement(self):
        self.move(960, 138)
        pyautogui.leftClick()
    def changeDurationTime(self):
        self.move(331, 200)
        pyautogui.leftClick()
        self.delay(0.5)
        self.move(777, 503)
        pyautogui.leftClick()
        self.delay(0.5)
        '''
        self.move(641, 574)
        pyautogui.leftClick()
        self.delay(2.0)
        '''
        self.move(769, 647)
        pyautogui.leftClick()
        self.delay(0.5)
    def clickOKSetting(self):
        self.move(1179, 683)
        pyautogui.leftClick()
        self.delay(0.5)
    def clickSAVE(self):
        self.move(71, 581)
        while True:
            self.move(71, 581)
            if self.btn_status(71, 581) == (229, 241, 251):
                break
            self.delay(0.5)
            self.move(70, 580)
            self.delay(0.5)
        pyautogui.leftClick()
        self.delay(0.5)
    def typeFileNameAndSave(self, fname):
        self.move(405, 417)
        pyautogui.leftClick()
        self.delay(0.5)
        pyautogui.write(fname)
        self.move(529, 448)
        pyautogui.leftClick()
        self.delay(0.5)

def main():
    print('Autoclick V-MER')
    mouse = Mouse()
    print('clickVibrationMeasurement')
    mouse.clickVibrationMeasurement()
    print('changeDurationTime')
    mouse.changeDurationTime()
    print('clickOKSetting')
    mouse.clickOKSetting()
    print('clickSAVE')
    mouse.clickSAVE()
    mouse.typeFileNameAndSave('savefrom_AuToClick')
    while True:
        if mouse.btn_status(69, 688) != (255, 255, 255):
            mouse.click(69, 688)
            mouse.delay(0.5)
            mouse.move(961, 139)
            mouse.delay(0.5)
            mouse.move(960, 138)
            mouse.delay(0.5)
        elif mouse.btn_status(960, 138) == (229, 241, 251):
            break
        mouse.delay(1.0)
    print('END')

if __name__ == "__main__":
    main()