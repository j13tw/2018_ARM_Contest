import os, sys
from serial import SerialException
from flask import Flask, request, render_template, redirect, url_for
from NFC_Class import NFC
from STM32_Class import STM32
from LORA_Class import LORA
import time

NFC_locate = "COM6"
STM32_locate = "COM3"
LORA_locate = "COM8"

# fake data 

# system boot up
def Client_hotware_boot():
    # STM32_check_device
    stm32 = STM32()
    nfc = NFC()
    lora = LORA()
    print("STM32_check")
    while (1):
        if (stm32.STM32_boot(STM32_locate) == "OK"):
            break
        else:
            print("check_STM32_port\n")
        time.sleep(1)
    print("STM32_check_boot")
    while(1):
        if (stm32.STM32_response("STM32") == "OK"):
            stm32.STM32_write("STM32")
            break
        time.sleep(1)
    # RFID_check_device
    print("RFID_check")
    while(1):
        if (stm32.STM32_response("RFID") != "OK"):
            while(1):
                if (nfc.NFC_boot(NFC_locate) == "OK"):
                    if (nfc.NFC_wake() == "OK"):
                        stm32.STM32_write("RFID")
                        break
                    else:
                        print("RFID_ERROR")
                else:
                    print("RFID_PORT_ERROR")
            break
        time.sleep(1)
    # LORA_check_device
    while(1)
        if (STM32.STM32_response("LORA") == "OK"):
            if (lora.LORA_boot(LORA_locate) == "OK"):
                if (lora.LORA_write("AT") == "OK"):
                    STM32_write("LORA")
                    break
                else:
                    print("LORA_ERROR") 
            else:
                print("LORA_PORT_ERROR")
        time.sleep(1)
    

#def Client_software_boot():

while (1):
    Client_hotware_boot()
