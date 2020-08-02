import web

import mvc.models.personas as personas
model_personas = personas.Personas()


render = web.template.render("mvc/views/modulos")

class View():
    def GET(self, id_persona):
        try:
            result = model_personas.view(id_persona)[0]
            return render.view(result) 
        except Exception as e:
            return "Error" + str(e.args)

    def POST(self):
        try: 
            form = web.input()
            print (type(form))
            print (form)
        except Exception as e:
            return "Error" + str(e.args)