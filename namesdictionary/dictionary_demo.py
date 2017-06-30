f=open("b.txt",'r')
nameslist=f.read().split(",")
print(nameslist)

for i in range(len(nameslist)):
	for j in range(len(nameslist)-1):
		if(nameslist[i]<nameslist[j]):
			temp=nameslist[i]
			nameslist[i]=nameslist[j]
			nameslist[j]=temp

print(nameslist)

namesdictionary={}
for n in nameslist:
	listnew=[]
	if(n[0] not in namesdictionary):
		listnew.append(n)
	elif(n[0] in namesdictionary):
		listnew.append(n)
	namesdictionary[n[0]]=listnew
		

for k,v in namesdictionary.items():
	print(k,v)


# using the sorted function available
# sortedlist=sorted(nameslist)
# print(sortedlist)