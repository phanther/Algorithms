import os, sys

def pascals_tri(n):
	a = [[0 for x in range(n)] for x in range(n)]
	a[0][0] = 1
	for i in range(1,n):
		a[i][0] = 1
		for j in range(1,n-1):
			a[i][j] = a[i-1][j-1] + a[i-1][j]
		a[i][i] = 1
       	
	return a 
       
n=int(sys.argv[1]) 
res = pascals_tri(n)
print "n: %i" % n
for x in range(len(res)):
	print res[x]
