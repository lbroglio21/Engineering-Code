import math 
monthCount=1

leapYear=False
February=False
dayOfWCount=2
dayOfMCount=1

year=1901
sunOnFirst=0


for year in range(1901,2000):
	MOY=1
	print(sunOnFirst)
	for MOY in range(12):
		DOM=1
		if MOY==4 or MOY==6 or MOY==9 or MOY==11:
			mLength=30
		elif MOY==2 and year%4==0:
			mLength=29
		elif MOY==2:
			mLength=28
		else:
			mLength=31	
		for DOM in range(mLength):
			
		
		
			
			if dayOfWCount==7 and DOM ==1:
				sunOnFirst+=1	
			dayOfWCount+=1
			
			if dayOfWCount==8:
				dayOfWCount=1
		
