import serial, time
from serial import SerialException

class LORA():
    def __init__(self):
        self.buad = 115200
        self.LORA_locate = ""

#   check USB is mount on the rpi3 command
    def LORA_boot(self, tty="COM3"):
        self.LORA_locate = tty
        try:
            ser = serial.Serial(self.LORA_locate, self.buad, timeout=1)
            ser.close()
            return "OK"
        except:
            return "ERROR"

#   check device and setup configure command
    def LORA_write(self, write_command):
        try:
            ser = serial.Serial(self.LORA_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        write_command = write_command + '\r'
        ser.write(bytes(write_command, 'ascii'))
        response = ser.read(1000)
        ser.close()
#        print(response)
        response = response.decode('ascii').split()
#        print(response)
        for x in range(0, len(response)):
            if (response[x] == "OK"):
                return "OK"
        return "ERROR"


#   send search / write MongoDB data command
    def LORA_send(self, write_command):
        try:
            ser = serial.Serial(self.LORA_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        write_command = write_command + '\r'
        ser.write(bytes(write_command, 'ascii'))
        ser.read(1000)
        response = ser.read(500)
        ser.close()
        response = response.decode('ascii').split('\r\n')[0]
        return response
