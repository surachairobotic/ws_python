import serial
import serial.tools.list_ports

class Yamaha():
    def __init__(self):
        self.id = "DTA3660FA"
        self.port = ""

    def init(self):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if self.id in hwid:
                self.port = port
        if self.port is "":
            print("Yamaha device not found.")
            return False

        print("Yamaha port name : " + self.port)
        self.ser = serial.Serial(self.port,
                                 38400,
                                 bytesize=serial.EIGHTBITS,
                                 parity=serial.PARITY_ODD,
                                 stopbits=serial.STOPBITS_ONE,
                                 timeout=1)
        my_str = "@?D0.1\r\n"
        my_str_as_bytes = str.encode(my_str)
        self.ser.write(my_str_as_bytes)
        x = self.ser.read(100).decode()
        if not ("D0.1" in x and "OK" in x):
            return False
        return True

    def tmp():
        #print(self.ser.name)
        #print(self.ser.is_open)
        c=0
        cmd = [0,1,2,6,7,9,10,13,14,17,18]
        cmd_desc = ["Current position",
                    "Current speed",
                    "Electrical current",
                    "Position command",
                    "Speed command",
                    "Voltage value",
                    "Temperature",
                    "Current point number",
                    "Load rate",
                    "Machine reference",
                    "Operation status"]
        for i in range(len(cmd)):
            my_str = "@?D" + str(cmd[i]) + ".1\r\n"
            my_str_as_bytes = str.encode(my_str)
            self.ser.write(my_str_as_bytes)
            x="--"
            while len(x)>0:
                x = self.ser.read(100)
                c = c+1
                if len(x)>0:
                    x = x.decode().split()
                    print("[" + str(cmd[i]) + "] : " + x[0] + "\t" + cmd_desc[i])
                    #print(str(type(x)))
                    #print(str(len(x)))
        #print("Loop ending ...")
        self.ser.close()
        #print(self.ser.is_open)
