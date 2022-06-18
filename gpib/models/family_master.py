from odoo import api, fields, models


class FamilyMaster(models.Model):
    _name = "gpib.family.master"
    _description = "Family Master"

    name = fields.Char(string='Name', required=True)
    qty = fields.Integer(string='Qty', required=True)
    address = fields.Text(string='Address', required=True)
    sector_id = fields.Many2one(string='Name Sector', required=True)