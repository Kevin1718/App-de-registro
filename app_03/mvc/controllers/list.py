import web 
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

render = web.template.render("mvc/views/")

class List():
    def GET(self):
        try:
            return render.list() 
        except Exception as e:
            return "Error" + str(e.args)