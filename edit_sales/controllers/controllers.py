# from odoo import http


# class EditSales(http.Controller):
#     @http.route('/edit_sales/edit_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_sales/edit_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_sales.listing', {
#             'root': '/edit_sales/edit_sales',
#             'objects': http.request.env['edit_sales.edit_sales'].search([]),
#         })

#     @http.route('/edit_sales/edit_sales/objects/<model("edit_sales.edit_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_sales.object', {
#             'object': obj
#         })

