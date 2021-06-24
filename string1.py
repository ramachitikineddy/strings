def findnumbers(s):
p= len(s)
count=1
result=0
left=0
right=1
while(right<p):
    if (s[left]==s[right]):
        count+=1
    else:
        result+=count*(count+1)//2
        left=right
        count=1
    right+=1
    result+=count*(count+1)//2
    print(result)
s="bbbcb"
findnumbers(s)
    
    
               
