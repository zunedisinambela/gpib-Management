from odoo import api, fields, models


class Pelkat(models.Model):
    _name = "gpib.pelkat"
    _description = "App Pelkat"

    name = fields.Char(string='Name', required=True)
    group_gender = fields.Selection([
        ('all', 'All'),
        ('male', 'Male'),
        ('female', 'female'),
    ], required=True, default='all')
    is_married = fields.Boolean(default=False)
    age_min = fields.Integer(default=0)
    age_max = fields.Integer(default=60)
