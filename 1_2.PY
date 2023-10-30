A=48
ad=0
for i in range(1, int(A**(1/2)+1)):
    if A%i==0:
        ad+=i
        if A/i!=A:
            ad+=(A/i)
print(ad)