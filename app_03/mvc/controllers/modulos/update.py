import web 

import mvc.models.personas as personas

model_personas = personas.Personas()
render = web.template.render("mvc/views/modulos")

class Update():
    def GET(self, id_persona):
        try:
            result = model_personas.view(id_persona)[0]
            return render.update(result) 
        except Exception as e:
            print(e)
            return "Error"

    def POST(self, id_persona):
            try: 
                form = web.input()
                id_persona = form.id_persona
                nombre = form.nombre
                apellido_p = form.apellido_p
                apellido_m = form.apellido_m
                edad = form.edad
                fecha_nacimiento = form.fecha_nacimiento
                genero = form.genero 
                estado = form.estado
                result = model_personas.update(id_persona,nombre,apellido_p,apellido_m,edad,fecha_nacimiento,genero,estado)
                web.seeother('/list')
            except Exception as e:
                print(e)
                return "Error"