	#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#This imports the Drivers for leds strips of type LPD8806 and sets it up
from bibliopixel.drivers.LPD8806 import *
driver = DriverLPD8806(num = 32, c_order= ChannelOrder.GRB, SPISpeed = 16) #SPI$

#Import leds info and set up
from bibliopixel.leds import *
leds = ledsStrip(driver)

#Import and setup test animation
from bibliopixel.animation import *
anim1 = StripChannelTest(leds)

#Import and setup test animation
#from strip_animation import *
#anim = RainbowCycle(leds)


try:

        leds.fillRGB(r = 50, g = 50, b = 0,start = 0, end = 0)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 1, end = 1)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 2, end = 2)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 3, end = 3)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 4, end = 4)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 5, end = 5)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 6, end = 6)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 7, end = 7)
	leds.fillRGB(r = 255, g = 255, b = 255, start = 8, end = 8)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 9, end = 9)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 10, end= 10)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 11, end= 11)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 12, end= 12)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 13, end= 13)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 14, end =14)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 15, end= 15)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 16, end = 16)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 17, end = 17)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 18, end = 18)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 19, end = 19)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 20, end = 20)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 21, end = 21)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 22, end = 22)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 23, end = 23)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 24, end = 24)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 25, end = 25)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 26, end = 26)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 27, end = 27)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 28, end = 28)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 29, end = 29)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 30, end = 30)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 31, end = 31)
        leds.fillRGB(r = 255, g = 255, b = 255, start = 32, end = 32)
        leds.update()
except KeyboardInterrupt:
        leds.all_off()
        leds.update()
        
