n = 3
for i in range(2,n):
    if n % i == 0:
        print("not prime")
        exit()
print("prime")