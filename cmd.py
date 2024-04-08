import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	datas=data.split(";")
	for n in datas:
		srun(n)
	
def sline(argvs):
	
	n=" "
	while 1:
		n=input(" BLUE> ")
		if n!="":
			if n!="\n":
				if n=="EXIT":
				    return None
				if n=="exit":
				    return None 	
				scommand(n)
			else:
			    return None	
		else:
		    return None		
	
	
print("\x1bc\x1b[44;37m")	
if 0==0:
	sline("stdio")
