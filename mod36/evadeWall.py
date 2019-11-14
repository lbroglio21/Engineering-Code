import RoboPiLib as RPL
import setup
import post_to_web as PTW

sensor_pin = 16
sensor_pin1 = 17
RPL.pinMode(sensor_pin,RPL.INPUT)
RPL.pinMode(sensor_pin1,RPL.INPUT)
running=True
wallSeen = False
seenTwice = False
m1Speed = 1400 
m2Speed = 1600

while running:
    reading=RPL.digitalRead(sensor_pin)
    reading1=RPL.digitalRead(sensor_pin1)
    if reading ==0:
        wallSeen  = True

    if wallSeen == True and seenTwice==False:
        m2Speed-=50
        seenTwice=True
    elif wallSeen == False and reading1==0:
        m2Speed=1600
        seenTwice=False

    if m1Speed == 1500 and m2Speed == 1500:
        m1Speed =00
        m2Speed =00
        running=False

    RPL.servoWrite(0,m1Speed)
    RPL.servoWrite(1,m2Speed)
        
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    PTW.state['d2'] = RPL.servoRead(0)
    PTW.state['d3'] = RPL.servoRead(1)
    PTW.post()
   
