from odoo import api, fields, models


class GpibSector(models.Model):
    _name = "gpib.sector"
    _description = "App Sector"

    name = fields.Char(string='Name', required=True)
    qty = fields.Integer(string='Qty')
