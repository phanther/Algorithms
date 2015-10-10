import sys, os
import math

def find_prime(num):
    try:
        n = long(num)
    except:
        n = long(float(num))
   
    if(n==1 or n==2):
        return True
    
    if n%2==0:
	return False

    for i in xrange(3, long(math.sqrt(n)), 1):
	if n%i==0:
	    return False

    return True

print find_prime(sys.argv[1])            
