import os
import os.path

def GetDirList(url):
	ls=os.listdir(url)
	dirlist={}
	for f in ls:
		p=os.path.join(url,f)
		if os.path.isdir(p):
			dirlist[f]=GetDirList(p)
		else:
			dirlist[f]=0
	return dirlist

def GetDirListHtml(url):
	ls=os.listdir(url)
	dirlisthtml="<div 'position'='relative','margin-left'='50px'>"
	for f in ls:
		p=os.path.join(url,f)
		if os.path.isdir(p):
			dirlisthtml=dirlisthtml+GetDirListHtml(p)
		else:
			dirlisthtml=dirlisthtml+"<p>"+f+"</p></br>"
	dirlisthtml=dirlisthtml+"</div>"
	return dirlisthtml