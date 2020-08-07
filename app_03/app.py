import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/', 'mvc.controllers.index.Index',
    '/delete/(.*)', 'mvc.controllers.modulos.delete.Delete',
    '/insert', 'mvc.controllers.modulos.insert.Insert',
    '/update/(.*)', 'mvc.controllers.modulos.update.Update',
    '/view/(.*)', 'mvc.controllers.modulos.view.View',
    '/list', 'mvc.controllers.modulos.list.List'

)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()