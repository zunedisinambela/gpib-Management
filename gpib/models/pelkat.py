from odoo import api, fields, models


class Pelkat(models.Model):
    _name = "gpib.pelkat"
    _description = "App Pelkat"

    name = fields.Char(string='Name', required=True)