import web 


render = web.template.render("mvc/views/modulos")

class Delete():
    def GET(self):
        try:
            return render.delete() 
        except Exception as e:
            return "Error" + str(e.args)
    def POST(self):
            try: 
                form = web.input()
                print(form)
            except Exception as e:
                return "Error" + str(e.args)
