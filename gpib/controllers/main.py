from odoo import http
from odoo.http import request


class Gpib(http.Controller):
    @http.route('/homepage', website=True, auth='user')
    def gpib(self, **kwargs):
        sectors = request.env['gpib.sector'].sudo().search([])
        families = request.env['gpib.family'].sudo().search([])
        values = {
            'name': 'zunedi',
            'age': 24,
            'sectors': sectors,
            'families': families
        }
        return request.render("gpib.gpib_template", values)
