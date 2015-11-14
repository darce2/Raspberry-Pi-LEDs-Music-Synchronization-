
#This imports the Drivers for LED strips of type LPD8806 and sets it up
from bibliopixel.drivers.LPD8806 import *
driver = DriverLPD8806(num = 32, c_order= ChannelOrder.GRB, SPISpeed = 16) #SPI speed still isn't fully understood but this value seems to work

#Import led info and set up
from bibliopixel.led import *
led = LEDStrip(driver)

#Import and setup test animation
#from bibliopixel.animation import *
#anim1 = StripChannelTest(led)

#Import and setup test animation
#from strip_animation import *
#anim = RainbowCycle(led)


##Turn off LED's
led.all_off()
led.update()

