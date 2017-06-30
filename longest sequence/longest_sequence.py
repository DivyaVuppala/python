f = open("a.txt",'r')
list_of_numbers = f.read().split(",")

integerlist=[]
for number in list_of_numbers:
	convertednumber=int(number)
	integerlist.append(convertednumber)

print(integerlist)
max=0	
for number in integerlist:
	numlist = []
	count=0
	while(number>0):
		temp = number % 10
		numlist.append(temp)
		number = number/10
	print numlist
	for i in range(len(numlist)):
		if (numlist[0]==numlist[i]):
			count=count+1
		elif (numlist[0]!=numlist[i]):
			count=0
			break
	print(count)
	if(count>=max):
		max=count


print(max)

