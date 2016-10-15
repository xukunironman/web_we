import web

urls=(
'/',"home",
'/photo','photo')
render=web.template.render('templates/')


class home:
	def GET(self):
		return render.home()

class photo:
	def GET(self):
		return render.photo()
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()
	
