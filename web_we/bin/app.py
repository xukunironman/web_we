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
			elif req=="datatime":
				p="datas/time.txt"
				(code,ls)=ReadList(p)
				if code==0:				#No Error
					datatimelist=ls[-1].split('-')
					datatimedic={"yea":datatimelist[0],"mon":datatimelist[1],"day":datatimelist[2],"hou":datatimelist[3],"min":datatimelist[4],"sec":datatimelist[5]}		
					valdic={"status":"OK","value":datatimedic}
					print("No error :"+valdic)
				else :
					print("Error:"+ls)
					valdic={"status":"WRONG","value":"No data in database"}
				return json.dump(valdic)
class admin:
	def GET(self):
		return render.admin()
		
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
	
