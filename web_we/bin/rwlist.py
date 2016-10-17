import os
import os.path

initString="This is the first string in this file"

ErrorDic={"FileNotExist":(1,"The file doesn't exist")}

'''
List file structure:
string:
ls1,ls2,ls3
'''
def ReadList(url):
	if os.path.exists(url)==False:  	#file not exist
		return ErrorDic["FileNotExist"]
	else:
		with open(url,'w') as f:
			strls=f.read()
			list=strls.split(',')
			return (0,list)

def WriteList(url,ls,mode="a"):	
	if os.path.exists(url)==False:  	#file not exist
		with open(url,'w') as f:		#create file
			f.write(initString)
	if mode=="a":						#add ls to this file
		with open(url,'at') as f:
			f.write(ls)
	elif mode=="w":					#rewrite ls to this file
		with open(url,'wt') as f:
			f.write(ls)	