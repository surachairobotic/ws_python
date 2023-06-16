import pyautogui, time, keyboard, schedule
from PIL import ImageGrab
import sys, os, traceback, types

class Mouse():
    def delay(self, t):
        time.sleep(t)
    def btn_status(self, x, y):
        #screen = ImageGrab.grab()
        #color = screen.getpixel((x, y))
        color = pyautogui.screenshot().getpixel((x, y))
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
        self.move(641, 574)
        pyautogui.leftClick()
        self.delay(2.0)
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
        with pyautogui.hold('ctrl'):
            pyautogui.press('a')
        pyautogui.press('backspace')
        pyautogui.write(fname)
        self.move(529, 448)
        pyautogui.leftClick()
        self.delay(0.5)

def autoclick():
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
    for i in range(5):
        mouse.click(69, 688)
        mouse.delay(1.0)
    print('END')

def main():
    
    while True:
        current_time = time.localtime()
        print(current_time)
        print(current_time.tm_min)
        if current_time.tm_min%5 == 0:
            autoclick()
            time.sleep(61)
        time.sleep(1)

def isUserAdmin():

    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        print("RuntimeError : Unsupported operating system for this module: {}".format(os.name))

def runAsAdmin(cmdLine=None, wait=True):

    if os.name != 'nt':
        print("RuntimeError : This function is only implemented on Windows.")

    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType,types.ListType):
        print("ValueError : cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    # XXX TODO: isn't there a function or something we can call to massage command line params?
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    #showCmd = win32con.SW_HIDE
    lpVerb = 'runas'  # causes UAC elevation prompt.

    # print "Running", cmd, params

    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
    # of the process, so we can't get anything useful from it. Therefore
    # the more complex ShellExecuteEx() must be used.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']    
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        #print "Process handle %s returned code %s" % (procHandle, rc)
    else:
        rc = None

    return rc

def test():
    rc = 0
    if not isUserAdmin():
        print("You're not an admin.", os.getpid(), "params: ", sys.argv)
        #rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
        rc = runAsAdmin()
    else:
        print("You are an admin!", os.getpid(), "params: ", sys.argv)
        rc = 0
    x = raw_input('Press Enter to exit.')
    return rc

if __name__ == "__main__":
    if not isUserAdmin():
        runAsAdmin()
    main()