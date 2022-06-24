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

    @api.model
    def get_data(self):

        sectors = self.env['gpib.sector'].search([])

        data_sectors = []
        for sector in sectors:
            data_sector = {
                'name': sector.name,
                'qty': sector.qty
            }
            data_sectors.append(data_sector)

        return data_sectors
