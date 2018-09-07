import serial, time
from serial import SerialException

class STM32():
    def __init__(self):
        self.buad = 9600
        self.STM32_locate = ""

    def STM32_boot(self, tty="COM3"):
        self.STM32_locate = tty
        try:
            ser = serial.Serial(self.STM32_locate, self.buad, timeout=1)
            ser.close()
#            print("OK\n")
            return "OK"
        except:
#            print("ERROR\n")
            return "ERROR"

    def STM32_response(self, check_item):
        try:
            ser = serial.Serial(self.STM32_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        response = ser.read(len(check_item))
        ser.close()
#        print(response.decode('ascii'))
#        print(check_item)
        if (response.decode('ascii') == check_item):
#            print("OK")
            return "OK"
        else:
#            print("ERROR")
            return "ERROR"

    def STM32_write(self, write_command):
        try:
            ser = serial.Serial(self.STM32_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        write_command = write_command + '\r\n'
        ser.write(bytes(write_command,'ascii'))