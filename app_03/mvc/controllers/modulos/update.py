import web 


render = web.template.render("mvc/views/modulos")

class Update():
    def GET(self):
        try:
            return render.update() 
        except Exception as e:
            return "Error" + str(e.args)

    def POST(self):
            try: 
                form = web.input()
                print (type(form))
                print (form)
            except Exception as e:
                return "Error" + str(e.args)