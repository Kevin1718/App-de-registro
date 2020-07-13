import web 

render = web.template.render("mvc/views/modulos")

class Insert():
    def GET(self):
        try:
            return render.insert() 
        except Exception as e:
            return "Error" + str(e.args)
    
    def POST(self):
        try: 
            form = web.input()
            print (type(form))
            print (form)
        except Exception as e:
            return "Error" + str(e.args)