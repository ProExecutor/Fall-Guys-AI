import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'H' in keys:
        return 'H'
    elif 'B' in keys:
        return 'B'
    elif 'A' in keys:
        return 'A'
    elif 'D' in keys:
        return 'D'
    elif ' ' in keys:
        return ' '
    else:
        return 'W'

while True:
    print(key_check())
    time.sleep(0.1)
    if 'Q' in key_check():
        break
