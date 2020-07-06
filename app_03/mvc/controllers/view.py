import web 
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

render = web.template.render("mvc/views/")

class View():
    def GET(self):
        try:
            return render.view() 
        except Exception as e:
            return "Error" + str(e.args)