import math 
import time
import os

f=0

width= os.get_terminal_size().columns-2

while True:
    f+=0.05
    sinew=(math.sin(f)*(width/2))+(width/2)
    cosw=(math.cos(f)*(width/2))+(width/2)
    tanw=(math.tan(f)*(width/2))+width
    tstr=""
    for i in range(width+1):
        if round(tanw)==i:
            tstr+="A"
        elif round(sinew)==i:
            tstr+="B"
        elif round(cosw)==i:
            tstr+="C"
        else:
            tstr+=" "
    print(tstr)
    time.sleep(0.01)