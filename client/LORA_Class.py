import serial, time
from serial import SerialException

class LORA():
    def __init__(self):
        self.buad = 115200
        self.LORA_locate = ""

    def LORA_boot(self, tty="COM3"):
        self.LORA_locate = tty
        try:
            ser = serial.Serial(self.LORA_locate, self.buad, timeout=1)
            ser.close()
#            print("OK\n")
            return "OK"
        except:
#            print("ERROR\n")
            return "ERROR"

    def LORA_write(self, write_command):
        try:
            ser = serial.Serial(self.LORA_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        write_command = write_command + '\r'
        ser.write(bytes(write_command, 'ascii'))
        response = ser.read(200)
        ser.close()
        response = response.decode('ascii').split()[1]
        if (response == "OK"):
            print("OK")
            return "OK"
        else:
            print("ERROR")
            return "ERROR"
