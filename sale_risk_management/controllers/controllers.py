# from odoo import http


# class SaleRiskManagement(http.Controller):
#     @http.route('/sale_risk_management/sale_risk_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_risk_management/sale_risk_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_risk_management.listing', {
#             'root': '/sale_risk_management/sale_risk_management',
#             'objects': http.request.env['sale_risk_management.sale_risk_management'].search([]),
#         })

#     @http.route('/sale_risk_management/sale_risk_management/objects/<model("sale_risk_management.sale_risk_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_risk_management.object', {
#             'object': obj
#         })

