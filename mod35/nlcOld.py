import math 
count=0

for i in range (11):


	if i==1 or i==2 or   i==6:
		count+=3
	elif i==3 or i==7 or i==8:
		count+=5
	elif i==4 or i==5 or i==9:
		count+=4
count*=9

for b in range(11,21):
	if b==11 or b==12 or b==15 or b==16:
		count+=7
	elif b==19 or b==18 or b==14 or b==13:
		count+=8

for q in range (11):
	if q ==1:
		count+=3
	if q==7:
		count+=70
	if q==9 or q==8 or q==2 or q==3:
		count+=60*4
	if q==4 or q==5 or q==6:
		count+=50*3 
count*10
for w in range(11):
	if w ==10:
		count+=10 

	if w==1 or w==2 or   w==6:
		count+=10*100*4

	elif w==3 or w==7 or w==8:
		count+=12*100*3
	elif w==4 or w==5 or w==9:	
		count+=11*100*3
print(count)	
