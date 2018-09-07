import os, sys
from serial import SerialException
from flask import Flask, request, render_template, redirect, url_for
from NFC_Class import NFC
from STM32_Class import STM32
import time

NFC_locate = "COM6"
STM32_locate = "COM3"
LORA_locate = "COM8"

# fake data 

# LORA check "mod get_ver"
def LORA_response(STM32_locate):
    return "OK"

# system boot up
def Client_hotware_boot():
    # STM32_check_device
    stm32 = STM32()
    nfc = NFC()
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
                if (nfc.wake(NFC_locate) == "OK"):
                    stm32.STM32_write("RFID")
                    break
                else:
                    print("RFID_ERROR")
            break
        time.sleep(1)
    # LORA_check_device
    while (STM32.STM32_response(STM32_locate) != "LORA"):
        if (LORA.LORA_response(LORA_locate(LORA_locate)) == "OK"):
            STM32_write("LORA")
        else:
            print("LORA_ERROR")
    

#def Client_software_boot():

while (1):
    Client_hotware_boot()
