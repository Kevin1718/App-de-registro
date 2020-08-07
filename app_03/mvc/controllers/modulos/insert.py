import web 

import mvc.models.personas as personas

model_personas = personas.Personas()

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
            nombre = form.nombre
            apellido_p = form.apellido_p
            apellido_m = form.apellido_m
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            genero = form.genero 
            estado = form.estado
            model_personas.insert( nombre, apellido_p, apellido_m, edad, fecha_nacimiento, genero, estado)
            web.seeother('/list')
            print(form)

        except Exception as e:
            print(e)
            print(form)