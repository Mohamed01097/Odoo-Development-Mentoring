# from odoo import http


# class OdooMentoring(http.Controller):
#     @http.route('/odoo_mentoring/odoo_mentoring', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_mentoring/odoo_mentoring/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_mentoring.listing', {
#             'root': '/odoo_mentoring/odoo_mentoring',
#             'objects': http.request.env['odoo_mentoring.odoo_mentoring'].search([]),
#         })

#     @http.route('/odoo_mentoring/odoo_mentoring/objects/<model("odoo_mentoring.odoo_mentoring"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_mentoring.object', {
#             'object': obj
#         })

