import yamaha
import laser
import keyboard as key
import time

base = yamaha.Yamaha()
laser = laser.Laser()

def main():
    global base, laser
    if not (base_init() and laser_init()):
        return False

    laser.laser.draw_rect()

    laser.laser.start_list(True)
    laser.laser.enable_laser(True)
    laser.laser.laser_on(True)
    for i in range(500):
        laser.laser.delay_one_ms()
    laser.laser.laser_on(False)
    laser.laser.enable_laser(False)
    laser.laser.start_list(False)
    laser.laser.exec_list(True)
    time.sleep(5)
    laser.laser.exec_list(False)
    '''
    en_on = [False, False]
    while True:
        if key.is_pressed('e'):
            en_on[0] = True
        else:
            en_on[0] = False
        if key.is_pressed('l'):
            en_on[1] = True
        else:
            en_on[1] = False
        print(en_on)
        laser.enable_laser(en_on[0])
        laser.laser_on(en_on[1])
        if key.is_pressed('q'):
            break
        time.sleep(0.1)
    '''

def base_init():
    global base
    if not base.init():
        print("Base init failed.")
        return False
    print("Base init passed.")
    return True

def laser_init():
    global laser
    if not laser.init():
        print("Laser init failed.")
        return False
    print("Laser init passed.")
    return True
    
if __name__ == "__main__":
    main()
