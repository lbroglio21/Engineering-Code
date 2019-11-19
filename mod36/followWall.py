import RoboPiLib as RPL
import setup
import post_to_web as PTW

sensor_pin=16
mSpeed=1400
mSpeed2=1600
Asensor_pin=1

running=True
while running:
	distance=RPL.analogRead(Asensor_pin)
	RPL.servoWrite(1,mSpeed2)
	RPL.servoWrite(0,mSpeed)
	
		
