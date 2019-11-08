import math 
count=0
countT=0
finalCount=0
tensPlace={
	0:0,
	2:6,
	3:6,
	4:5,
	5:5,
	6:5,
	7:7,
	8:6,
	9:6
}
hundredsPlace={
	1:10,
	2:10,
	3:12,
	4:11,
	5:11,
	6:10,
	7:12,
	8:12,
	9:11
}
#Gets count for one through-ten
def countSD (num):
	global count
	for i in range (1,int(num)+1):
		if i==1 or i==2 or   i==6:
			count+=3
		elif i==3 or i==7 or i==8:
			count+=5
		elif i==4 or i==5 or i==9:
			count+=4
	return count	
# Gets coutn for 11-19
def countTeens (num):	
	global countT 
	if num>10:
		for b in range(11,num+1):
			if b==11 or b==12 or b==15 or b==16:
				countT+=7
			elif b==19 or b==18 or b==14 or b==13:
				countT+=8
	return countT
# Counts rest of the numbers
def total(num):
	global finalCount
	global count 
	global countT
	countSD(num)
	finalCount+=count
	count=0
	countTeens(num)	
	finalCount+=countT
	countT=0
	for i in range(20,num+1):	
		if i<100:						
			FD=int(str(i)[:1])
			finalCount+=tensPlace[FD]
			SD=int(str(i)[:-1])
			countSD(SD)
			finalCount+=count
			count=0	
		elif i<1000:
			firstDigit=int(str(i)[:1])
			finalCount+=hundredsPlace[firstDigit]
			secondDigit=int(str(i)[:-2][:1])
			if secondDigit==1:
				F2=int(str(i)[:-2])
				countTeens(F2)
				finalCount+=countT
				countT=0
			else:
				finalCount+=tensPlace[secondDigit]
			thirdDigit=int(str(i)[:-1])
			countSD(thirdDigit)
			finalCount+=count
			count=0	
			if secondDigit!=0 and thirdDigit !=0:
				finalCount+=3
		if i==1000:
			finalCount+=11


number=input("Enter and integer between 1 and 1000 ")
number=int(number)
if number>1000 or number<1:
	print("that answer is invalid")
else:
	total(number)
	print(finalCount)



















































		
		





	
	
		
