import io
file=open("names.txt","r")
file_text=file.read()
arr=file_text.split(",")
indexarray=[]

def getIndexArrays(w):
	word=sorted(w)
	for i in range(len(arr)):
		if (word == sorted(arr[i])):
			indexarray.append(i)

getIndexArrays("print")

print(indexarray)

dict={}
for x in arr:
	getIndexArrays(x)
	dict[x]=indexarray
	indexarray=[]

for k,v in dict.items():
	print(k,v)


