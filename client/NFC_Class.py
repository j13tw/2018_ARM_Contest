import serial, time
from serial import SerialException

# wake up reader
# send: 55 55 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff 03 fd d4 14 01 17 00
# return: 00 00 FF 00 FF 00 00 00 FF 02 FE D5 15 16 00
 
# get firmware
# send: 00 00 FF 02 FE D4 02 2A 00
# return: 00 00 FF 00 FF 00 00 00 FF 06 FA D5 03 32 01 06 07 E8 00
 
# read the tag
# send: 00 00 FF 04 FC D4 4A 01 00 E1 00
# return: 00 00 FF 00 FF 00 00 00 FF 0C F4 D5 4B 01 01 00 04 08 04 XX XX XX XX 5A 00
# XX is tag.

class NFC():
    def __init__(self):
        self.wakeReader = bytearray([85, 85, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 3, 253, 212, 20, 1, 23, 0])
        self.deviceInfo = bytearray([0, 0, 255, 2, 254, 212, 2, 42, 0])
        self.readTag = bytearray([0, 0, 255, 4, 252, 212, 74, 1, 0, 225, 0])

    def wake(self, NFC_locate):
        ser = serial.Serial(NFC_locate, 115200, timeout=1)
        ser.write(self.wakeReader)
        Ack = str(ser.read(15)).upper().split('\\X')
#       response = "return wake block = "
        for x in range(1, len(Ack)):
            if x == len(Ack)-1:
                response = response + ' ' + Ack[x].split("'")[0]
            else:    
                response = response + ' ' + Ack[x]
#        print(response)
        if response != "": response = "OK"
        else: response = "ERROR"
        ser.close()
        return response

    def info(self, NFC_locate):
        ser = serial.Serial(NFC_locate, 115200, timeout=1)
        ser.write(self.deviceInfo)
        Ack = str(ser.read(19)).upper().split('\\X')
 #       response = "return info block = "
        for x in range(1, len(Ack)):
            if x == len(Ack)-1:
                response = response + ' ' + Ack[x].split("'")[0]
            else:    
                response = response + ' ' + Ack[x]
#        print(response)
        if response != "": response = "OK"
        else: response = "ERROR"
        ser.close()
        return response

    def read(self, NFC_locate):
        ser = serial.Serial(NFC_locate, 115200, timeout=1)
        ser.write(self.readTag)
        Ack = str(ser.read(45)).upper().split('\\X')
#        response = "return card block = "
        for x in range(10, 20):
            response = response + Ack[x]
#        print(response)
        if response == "": "ERROR"
        ser.close()
        return response