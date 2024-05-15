
from ClockController import *

mydisplay = LCDDisplay (sda=0, scl= 1, i2cid=0)


myclock = ClockController()

while True:
    mydisplay.showText("You did it!",row=1,col=1)
    myclock.showTime()
    time.sleep(1)
    