import sys
import math


def minimumMoves(s,d):
	count=0
	flag=False
	for i in range(len(s)):
		if(i>=(d-1) and i<=(len(s)-d)):
			for j in range(i-(d-1),i+(d-1)+1):
				if(s[j]==1):
					flag=True
	print(flag)



if __name__ == '__main__':  
	sys.stdin=open("pyIn.txt","r")
	fout=open("pyOut.txt","w")  
#---------------------------------

	s = input()

	d = int(input().strip())
#---------------------------------
	result=minimumMoves(s,d)
	fout.write(str(result) + "\n")
	fout.close()


	