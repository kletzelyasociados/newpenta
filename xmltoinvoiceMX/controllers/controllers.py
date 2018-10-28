from odoo import http


class MyModule(http.Controller):
     @http.route('/newpenta/xmltoinvoiceMX/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/newpenta/xmltoinvoiceMX/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('xmllisting', {
             'root': '/newpenta/xmltoinvoiceMX',
             'objects': http.request.env['xml'].search([]),
         })

     @http.route('/newpenta/xmltoinvoiceMX/objects/<model("xml"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('xml.object', {
             'object': obj
         })


