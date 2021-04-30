import keyboard 
import json 
import os 
import hashlib

with open('storage.json','r') as JsonFile:
    j = json.load(JsonFile)['password']

counter = []

def insert(x):
    counter.append(x)

keyboard.add_hotkey("1",lambda:insert(1))
keyboard.add_hotkey("0",lambda:insert(0))

keyboard.wait('esc')

k = hashlib.sha256()
h = ' '.join(list(map(str,counter)))
k.update(h.encode('utf-8'))
d = k.hexdigest()

if d==j :
    print('right password')
else:
    print('wrong password')
