#! /usr/bin/env python
import sys
import os
import time
import datetime
import copy
import configparser
from io import BytesIO
import irserial

KEY_USER_CODE = [0x01,0xFD]
bcm_ir = {
    "power":0xDC,
    "mute":0x9c,
    "num0":0x87,
    "num1":0x92,
    "num2":0x93,
    "num3":0xcc,
    "num4":0x8e,
    "num5":0x8f,
    "num6":0xc8,
    "num7":0x8a,  
    "num8":0x8b,
    "num9":0xc4,    
    "menu":0x95,
    "setup":0x10,
    "back":0x82,
    "exit":0xc5,
    "left":0x99,
    "right":0xc1,
    "up":0xCA,
    "down":0xd2,
    "ok":0xce,
    "info":0xd0,
    "epg":0xd6,
    "vol-":0xd6,
    "vol+":0x85,
    "ch-":0x81,
    "ch+":0x80,
    "diagnostics":0x83,
    "events":0xcd,
    "fav":0x88,
    "tvradio":0xd9,
    "red":0x96,
    "green":0xc2,
    "yellow":0xc3,
    "blue":0x84,
    "rewind":0x8d,
    "play":0x91,
    "forward":0xc9,
    "stop":0xcf,
    "list":0xda,
    "rec":0x9a,
    "audio":0x9d,
    "email":0x78,
    "txt":0x76,
    "LR":0x74,
}

# format : key +timeout(ms),
test_case1=[
    ['up',5000],
    ['ok',2000],
    ['up',2000], 
    ['exit',1000],
    ['down',5000], 
    ['right',1000],
    ['right',1000],
    ['exit',1000],
    ['exit',1000],
    ['power',5000],
    ['power',5000],
    ]

IRserialFd = IRserial.IRserial("COM10",9600,60)
start = datetime.datetime.now()
#([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
end = start+datetime.timedelta(minutes=3,hours=1)

while True:
    now  = datetime.datetime.now()
    if now > end:
        break
    for case in test_case1:
        key=copy.deepcopy(KEY_USER_CODE)
        key.append(bcm_ir[case[0]])
        if IRserialFd.send(key):
            print("send "+case[0]+" ok.")
        time.sleep(case[1]/1000)

print("Test end.")
IRserialFd.close()


