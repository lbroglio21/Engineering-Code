#import needed modules 
import math 
#Set up variables 
SqOS=0
SOSq=0
#loop
for i in range(100):
	temp1=i**2
	SqOS+=i
	SOSq+=temp1

print(SOSq)

SqOSF=SqOS**2
print(SqOSF)
diff=SqOSF-SOSq
print(diff)	
