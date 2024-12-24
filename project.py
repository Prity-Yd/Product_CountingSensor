from machine import Pin 
from time import sleep 
ir=Pin(4,Pin.IN) 
led=Pin(6,Pin.OUT) 
ir_val=0 
count=0 
s=False 
packet_count=0 
while True: 
x=ir.value() #fetching ir value 1 or 0 
if x==1: 
ir_val=0 
led.value(0) 
s=True 
else: 
ir_val=1 
led.value(1) 
if s==True: 
count=count+1 
s=False 
print(ir_val) 
if count==10: 
packet_count+=1 
count=0 
print('number:',count) 
print("Number of packet:",packet_count) 
sleep(0.3) 