import os, sys
from serial import SerialException
from flask import Flask, request, render_template, redirect, url_for
from NFC_Class import NFC


NFC_locate = "COM6"
STM32_locate = "COM7"
LORA_locate = "COM8"

# fake data 

def STM32_response(STM32_locate):
    return = "OK"

# LORA check "mod get_ver"
def LORA_response(STM32_locate):
    return = "OK"

# system boot up
def Client_hotware_boot():
    # STM32_check_device

    # RFID_check_device
    while (STM32.STM32_response(STM32_locate) != "RFID_CHECK"):
        if (NFC.wake(NFC.locate) == "OK"):
            STM32_write("RFID_OK")
        else:
            STM32_write("RFID_ERROR")
    # LORA_check_device
    while (STM32.STM32_response(STM32_locate) != "LORA_CHECK")
        if (LORA.LORA_response(LORA_locate(LORA_locate)) == "OK")
            STM32_write("LORA_OK")
        else:
            STM32_write("LORA_ERROR")
    

def Client_software_boot():

