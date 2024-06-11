n=121
temp=n
rev=0
while(n>0):
    digi=n%10
    rev=rev*10+digi
    n=n//10
if(temp==rev):
    print("palin")
else:
    print("not palin")