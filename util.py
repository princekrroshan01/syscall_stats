lines=[]
with open('file.txt','r') as f:
	lines = [line.rstrip() for line in f]
	

func=dict()
for item in lines:
	flag=0
	s=''
	for c in item:
		if(c=='('):
			flag=1
			break
		s+=c
	if(flag==1):
		if not func.get(s):
			func[s]=0
		func[s]=func[s]+1
	
for i,j in func.items():
	print("systemcall name",i,"\t\tnumber of calls",j)
	
if(__name__=='__main__'):
	import os
	os.system('python3 main.py && python3 util.py')
	f = open('file.txt', 'r+')
	f.truncate(0)
	exit(0)
	
