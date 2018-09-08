import os, sys
from serial import SerialException
from flask import Flask, request, render_template, redirect, url_for
from NFC_Class import NFC
from STM32_Class import STM32
from LORA_Class import LORA
import time

# config data
NFC_locate = "COM6"
STM32_locate = "COM3"
LORA_locate = "COM8"
DEVICE_id = "IMAC-001" 

# system hotware boot up
def Client_hotware_boot():
# make Class function to use 
    stm32 = STM32()
    nfc = NFC()
    lora = LORA()
# STM32_check_device
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
    while(1):
        if (stm32.STM32_response("LORA") == "OK"):
            if (lora.LORA_boot(LORA_locate) == "OK"):
                if (lora.LORA_write("AT") == "OK"):
                    stm32.STM32_write("LORA")
                    break
                else:
                    print("LORA_ERROR") 
            else:
                print("LORA_PORT_ERROR")
        time.sleep(1)
    
# LoRa_network_connect
def Lora_network_connect():
# make Class function to use / setup check config varible
    lora = LORA()
    errorCode = 0
# make LoRa wan connect config command
    if (lora.LORA_boot(LORA_locate) != "OK"): errorCode = 1
    if(lora.LORA_write("AT") != "OK" or errorCode == 1): errorCode = 1
    if(lora.LORA_write("AT&F") != "OK" or errorCode == 1): errorCode = 1
    if(lora.LORA_write("AT&W") != "OK" or errorCode == 1): errorCode = 1
    if(lora.LORA_write("AT+FSB=7") != "OK" or errorCode == 1): errorCode = 1
    if(lora.LORA_write("AT+NI=1,test12345") != "OK" or errorCode == 1): errorCode = 1
    if(lora.LORA_write("AT+NK=1,test12345") != "OK" or errorCode == 1): errorCode = 1
    if(lora.LORA_send("AT+JOIN") == "" or errorCode == 1):  errorCode = 1
    if(lora.LORA_write("AT+RXO=1") != "OK" or errorCode == 1):  errorCode = 1
    if(lora.LORA_write("AT+TXDR=DR3") != "OK" or errorCode == 1):  errorCode = 1
    return errorCode

# system hotware boot up
def Client_software_boot():
# use extern varable
    global DEVICE_id
# make Class function to use 
    stm32 = STM32()
    nfc = NFC()
    lora = LORA()
    nfc.NFC_wake()
# variable & data configure
    Card_id = nfc.readTag()
    Send_status = "R"
    Send_command = ""
    response = ""
# check system status
    if (Card_id != ""):
        Send_status = "R"
        Send_command = '{"status": "' + Send_status + '", "card_id": "' + Card_id + '", "device_id": "' + DEVICE_id + '"}'
        response = lora.LORA_send(Send_command)
        print(response)
        stm32.STM32_write(response)
        response = ""
    else:
        Client_software_boot()

while (1):
    Client_hotware_boot()
    if (Lora_network_connect() == 0):
        print("Network-OK")
        Client_software_boot()
    else:
        print("Network-ERROR")