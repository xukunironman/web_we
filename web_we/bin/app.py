import web

urls=(
	'/','Home'
	
)
render=web.template.render('templates')
class home:
	def GET(self):
		return render.Home()
	
if __name__=="__main__":
	app.run()
	