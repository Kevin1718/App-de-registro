import web 

import mvc.models.personas as personas

model_personas = personas.Personas()

render = web.template.render("mvc/views/modulos")

class Delete():
    def GET(self, id_persona):
        try:
            result = model_personas.view(id_persona)[0]
            return render.delete(result) 
        except Exception as e:
            print(e)
            return"Error"
    def POST(self, id_persona):
            try: 
                form=web.input()
                id_persona=form.id_persona
                result = model_personas.delete(id_persona)
                web.seeother('/list')
            except Exception as e:
                print(e)
                
