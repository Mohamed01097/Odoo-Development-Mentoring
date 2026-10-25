# from odoo import http


# class EditSale(http.Controller):
#     @http.route('/edit_sale/edit_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_sale/edit_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_sale.listing', {
#             'root': '/edit_sale/edit_sale',
#             'objects': http.request.env['edit_sale.edit_sale'].search([]),
#         })

#     @http.route('/edit_sale/edit_sale/objects/<model("edit_sale.edit_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_sale.object', {
#             'object': obj
#         })

