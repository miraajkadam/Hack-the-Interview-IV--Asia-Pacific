import sys
import math

def arrangeStudents(a, b):
    # Write your code here
    initial=[]
    initial.extend(a)
    initial.extend(b)
    initial.sort()
    q=[]
    true_arr=[]

    for i in range(len(initial)):
        if(initial[i] in a and initial[i] not in b):
            q.append(1)
        elif(initial[i] in b and initial[i] not in a):
            q.append(0)
        else:
            q.append('x')
    for i in range(0,len(q)-1,2):
        if((q[i]==1 and q[i+1]==0) or (q[i]==0 and q[i+1]==1) and (q[i]!='x')):
            true_arr.append(1)
        elif(q[i]=='x'):
            pass
        else:
            true_arr.append(0)
            
    if(0 in true_arr):
        return 'NO'
    else:
        return 'YES'




if __name__ == '__main__':  
	sys.stdin=open("pyIn.txt","r")
	fout=open("pyOut.txt","w")  
#---------------------------------

	t = int(input().strip())

	for t_itr in range(t):
		n = int(input().strip())

		a = list(map(int, input().rstrip().split()))

		b = list(map(int, input().rstrip().split()))
#---------------------------------
		result=arrangeStudents(a,b)
		fout.write(str(result) + "\n")
	fout.close()


	