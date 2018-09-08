
from LORA_Class import LORA

LORA_locate = "/dev/ttyACM0"

lora = LORA()

errorCode = 0

if (lora.LORA_boot(LORA_locate) != "OK"): errorCode = 1
print(errorCode)
if(lora.LORA_write("AT") != "OK" or errorCode == 1): errorCode = 1
print(errorCode)
if(lora.LORA_write("AT&F") != "OK" or errorCode == 1): errorCode = 1
print(errorCode)
if(lora.LORA_write("AT&W") != "OK" or errorCode == 1): errorCode = 1
print(errorCode)
if(lora.LORA_write("AT+FSB=7") != "OK" or errorCode == 1): errorCode = 1
print(errorCode)
if(lora.LORA_write("AT+NI=1,test12345") != "OK" or errorCode == 1): errorCode = 1
print(errorCode)
if(lora.LORA_write("AT+NK=1,test12345") != "OK" or errorCode == 1): errorCode = 1
print(errorCode)
if(lora.LORA_send("AT+JOIN") == " " or errorCode == 1):  errorCode = 1
print(errorCode)
if(lora.LORA_write("AT+RXO=1") != "OK" or errorCode == 1):  errorCode = 1
print(errorCode)
if(lora.LORA_write("AT+TXDR=DR3") != "OK" or errorCode == 1):  errorCode = 1
print(errorCode)
