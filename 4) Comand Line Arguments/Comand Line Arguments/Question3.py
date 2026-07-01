import sys
import math
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(math.isqrt(n))+1):
        if n%i == 0:
            return False
    return True

sum=0
for arg in sys.argv[1:11]:
    num=int(arg)
    if isPrime(num):
        sum+=num

print(sum)