import web

urls=(
'/',"home",
'/photo','photo',
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
			req=input[request]
		
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
	
