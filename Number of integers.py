import sys
import math


def getNumberOfIntegers(l,r,k):
	final=[]	
	count=0
	flag=False
	for i in range(int(l)+1,int(r)+1):
		# count=0
		if('0' not in str(i)):			
			if(len(str(i))==1):
				flag=True
			else:
				count+=1
	
	if(flag==True):
		return(((int(r)-int(l)) - count) % ((10**9)+7))
	else:
		return(count % ((10**9)+7))


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


	