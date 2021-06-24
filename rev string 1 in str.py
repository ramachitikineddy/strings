s=input()
d=s.split()
l=len(d)
for k in range(l-1,-1,-1):
    print(d[k],end=" ")
print('\n')


for i in d:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end="")
    print(end=" ")
print('\n')

for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
    
