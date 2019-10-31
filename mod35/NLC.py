import math 
count=0
countT=0
countTE=0
countH=9
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
		
# Gets coutn for 11-19
def countTeens (num):
	global countT
	for b in range(11,num+1):
		if b==11 or b==12 or b==15 or b==16:
			countT+=7
		elif b==19 or b==18 or b==14 or b==13:
			countT+=8

#Gets count for everytime 10-90 is used
def countTens(num):

	global countTE
	if num>=10:
		countTE+=3 
	if num>19 and num<29:
		countTE+=6*(num-19)
	elif num>29:
		countTE+=60
	if num>29 and num<39:
		countTE+=6*(num-29)

	elif num>39:
		countTE+=60

	if num>39 and num<49:
		countTE+=5*(num-39)
	elif num>49:
		countTE+=50
	if num>49 and num<59:
		countTE+=5*(num-49)
	elif num>59:
		countTE+=50
	if num>59 and num<69:
		countTE+=6*(num-59)
	elif num>69:
		countTE+=60
	if num>69 and num<79:
		countTE+=7*(num-69)
	elif num>79:
		countTE+=70
	if num>79 and num<89:
		countTE+=6*(num-79)
	elif num>89:
		countTE+=60
	if num>89 and num<99:
		countTE+=6*(num-89)
	elif num>99:
		countTE+=60
#Gets count for everytime 100-1000 is used
def countHundreds(num):
	global countH
	if num>99:
		if num<199:
			num2=num-99
			countH+=10*num2
		else:
			countH+=10*100		

	
	if num>199:
                if num<299:
                        num2=num-199
                        countH+=10*num2
                else:
                        countH+=10*100 
	if num>299:
		if num<399:     
			num2=num-299
                        countH+=12*num2
                else:
                        countH+=12*100 
			
	if num>399:
                if num<499:
                        num2=num-399
                        countH+=11*num2
                else:
                        countH+=11*100 

	if num>499:
                if num<599:
                        num2=num-499
                        countH+=11*num2
                else:
                        countH+=11*100 

	if num>599:
                if num<699:
                        num2=num-599
                        countH+=10*num2
                else:
                        countH+=10*100 
	if num>699:
                if num<799:
                        num2=num-699
                        countH+=12*num2
		else:
                        countH+=12*100 
			
	if num>799:
                if num<899:
                        num2=num-799
                        countH+=12*num2
                else:
                        countH+=12*100 
	if num>899:
                if num<999:
                        num2=num-899
                        countH+=11*num2
                else:
                        countH+=11*100 

	

def countNumOLet(num):
	finalCount=0
	countSD(num)
	
	finalCount+=count
	if num>10 and num<100:
		num2=num/10 
		num2=math.floor(num2)
		num2-=1
		finalcount+=(count*num2)
		num3=num/10
		num3-=math.floor(num3)
		num3*=10 
		countSD(num3)	
		finalCount+=count
	if num>100:
		num2=num/100
		num2=math.floor(num2)
		num2-=1
		countIH=count*10
		finalCount+=countIH
		countIH*=num2
		finalCount+=countIH
		num3=num/100
		num3-=math.floor(num3)
		num3*=10
		num3-=math.floor(num3)
		num3*=10 
		countSD(num3)
		finalCount+=count
	countTeens(num)
	finalCount+=countT
	countTens(num)
	finalCount+=countTE
	if num>100:
		num2=num/100
		num2=math.floor(num2)
		countTEH=countTE*(num2-1)
		finalCount+=countTEH 
		num3=num/100
		num3=num3-math.floor(num3)
		num3*=10 
		num3=math.floor(num3)
		countTens(num3)
		finalCount+=countTE
	countHundreds(num)
	finalCount+=countH
	if num==1000:
		finalCount+=11
	print("The number of letters in all the numbers leading up to yours is "+str(finalCount))

numUse=input("Choose an integer between 0 and 1000 ")
numUse1=int(numUse)
if numUse1>1000 or  numUse1 < 1 :
	print("That is not a valid choice")
else:
	countNumOLet(numUse1)	




	
		
		












		






















































		
		





	
	
		
