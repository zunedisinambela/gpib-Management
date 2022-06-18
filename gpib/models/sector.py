from odoo import api, fields, models


class GpibSector(models.Model):
    _name = "gpib.sector"
    _description = "App Sector"

    name = fields.Char(string='Name', required=True)
    qty = fields.Integer(string='Qty', compute='_compute_family')
    family_ids = fields.One2many('gpib.family', 'sector_id')

    def _compute_family(self):
        for record in self:
            record.qty = len(record.family_ids)
