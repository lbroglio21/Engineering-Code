import RoboPiLib as RPL
import setup
import post_to_web as PTW

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

running=True
braking = False
m1Speed = 1400 
m2Speed = 1600
while running:
    reading=RPL.digitalRead(sensor_pin)
    
    if reading ==0:
        braking = True
    else:
	braking=False
    if braking == True and m1Speed!=1490 and m2Speed!=1510:
        print("If statement fired")
        m1Speed+=10
        m2Speed-=10


    if m1Speed == 1490 and m2Speed == 1510:
	sleep(1)
	m1Speed+=10
	m2Speed-=10
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
   
