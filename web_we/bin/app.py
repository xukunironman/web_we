import web
import json
from rwlist import *
from getDirLs import *
urls=(
'/',"home",
'/photo','photo',
'/admin','admin'
'/request','request')
render=web.template.render('templates/')


class home:
	def GET(self):
		return render.home()

class photo:
	def GET(self):
		return render.photo()

class request:
	def GET(self):
		input=web.input()
		if "request" in input:
			req=input["request"]
			if req=="photolist":
				p='/static/image'
				ls=GetDirList(p)
				return json.dump(ls)
			elif req=="data":
				p="datas/time.txt"
				(code,ls)=ReadList(p)
				if code==0:				#No Error
					return ls[-1]
				else :
				print("Error:"+ls)
class admin:
	def GET(self):
		return render.admin()
		
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
	
