	#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#LPD8806 Initialization
from bibliopixel.drivers.LPD8806 import *
driver2 = DriverLPD8806(num = 64, c_order= ChannelOrder.GRB, SPISpeed = 16) #SPI$
from bibliopixel.led import *
led = LEDStrip(driver=driver2)

#Import and setup test animation
#from bibliopixel.animation import *
#anim1 = StripChannelTest(leds)

#Import and setup test animation
#from strip_animation import *
#anim = RainbowCycle(leds)

try:
        led.fillRGB(r=200,g=200,b=200,start=0,end = 31)
        led.update()
except KeyboardInterrupt:
        led.all_off()
        led.update()
        
