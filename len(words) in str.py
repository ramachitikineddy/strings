s=input()
data=s.split()
k=0
print(len(data))
for i in  range(len(data)):
    if len(data[i])>k:
        k=len(data[i])
        pos=i
print(pos+1,data[pos],k)

    
