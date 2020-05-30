import sys
import math


def getNumberOfIntegers(l,r,k):
	final=[]	

	for i in range(int(l)+1,int(r)+1):
		count=0
		# print(i)
		for j in str(i):
			if(int(j) != 0):
				count+=1
		final.append(count)

	return(final.count(k) % pow(10,9) + 7)


if __name__ == '__main__':	
	sys.stdin=open("pyIn.txt","r")
	fout=open("pyOut.txt","w")	
#---------------------------------

	L = input()

	R = input()

	K = int(input().strip())
#---------------------------------
	result=getNumberOfIntegers(L,R,K)
	fout.write(str(result) + "\n")
	fout.close()


	