import web

urls=(
	'/',home,
	
)
render=web.template.render('templates')
class home:
	def GET(self):
		return render.home()
	
if __name__=="__main__":
	app.run()
	