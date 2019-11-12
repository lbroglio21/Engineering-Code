import RoboPiLib as RPL
import setup
import post_to_web as PTW 

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
running=True 

while running:
     reading=RPL.digitalRead(sensor_pin)
     PTW.state['d1'] = RPL.digitalRead(sensor_pin)
     
     PTW.post()

