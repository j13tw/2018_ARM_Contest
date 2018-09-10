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
        self.NFC_locate = ""
        self.buad = 115200

    def NFC_boot(self, NFC_locate = "COM6"):
        try:
            ser = serial.Serial(NFC_locate, self.buad, timeout=1)
            self.NFC_locate = NFC_locate
            ser.close()
            return "OK"
        except:
            return "ERROR"

    def NFC_wake(self):
        try:
            ser = serial.Serial(self.NFC_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        ser.write(self.wakeReader)
        Ack = str(ser.read(15)).upper().split('\\X')
        ser.close()
        response = ""
        for x in range(1, len(Ack)):
            if x == len(Ack)-1:
                response = response + Ack[x].split("'")[0]
            else:    
                response = response + Ack[x] + ' '
#        print(response)
        if response == "00 00 FF 00 FF 00 00 00 FF 02 FE D5 15 16 00": response = "OK"
        else: response = "ERROR"
        return response

    def NFC_info(self):
        try:
            ser = serial.Serial(self.NFC_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        ser.write(self.deviceInfo)
        Ack = str(ser.read(19)).upper().split('\\X')
        ser.close()
 #       response = "return info block = "
        response = ""
        for x in range(1, len(Ack)):
            if x == len(Ack)-1:
                response = response + ' ' + Ack[x].split("'")[0]
            else:    
                response = response + ' ' + Ack[x]
#        print(response)
        if response != "": response = "OK"
        else: response = "ERROR"
        return response

    def NFC_read(self):
        try:
            ser = serial.Serial(self.NFC_locate, self.buad, timeout=1)
        except:
            return "ERROR"
        ser.write(self.readTag)
        Ack = str(ser.read(45)).upper().split('\\X')
        ser.close()
#        print(Ack)
        if (len(Ack) <= 7): return "ERROR"
#        response = "return card block = "
        response = ""
        for x in range(len(Ack)-4, len(Ack)-1):
            response = response + Ack[x]
#        print(response)
        return response