from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import datetime, date


class FamilyMaster(models.Model):
    _name = "gpib.family"
    _description = "Family Master"

    name = fields.Char(string='Name', required=True)
    qty = fields.Integer(string='Qty', compute='_compute_family_line')
    address = fields.Text(string='Address', required=True)
    sector_id = fields.Many2one('gpib.sector', string='Name Sector', required=True)
    line_ids = fields.One2many('gpib.family.line', 'family_id')

    def _compute_family_line(self):
        for record in self:
            record.qty = len(record.line_ids)


class FamilyLine(models.Model):
    _name = "gpib.family.line"
    _description = "Family Line"

    family_id = fields.Many2one(string='Family Name', required=True)
    name = fields.Char(string='Name', required=True)
    date_birthday = fields.Date(string='Date of Birth', required=True)
    date_baptism = fields.Date(string='Date of Baptis')
    date_sidi = fields.Date(string='Date of Sidi')
    last_education = fields.Char(string='Last Education')
    pelkat_id = fields.Many2one(string='Pelkat')
    age = fields.Integer(string='Age', compute='_compute_age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True)
    position = fields.Selection([
        ('KK', 'Kepala Keluarga'),
        ('IS', 'Istri'),
        ('AN', 'Anak'),
        ('OT', 'Orang Tua'),
        ('FA', 'Family')
    ], required=True)
    wedding_date = fields.Date(string='Wedding Date')
    state_married = fields.Selection([
        ('married', 'Married'),
        ('not_married', 'Not Married Yet'),
        ('divorced', 'Divorced'),
        ('death_divorce', 'Death Divorce')
    ], required=True, default='not_married')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('died', 'Died')
    ], required=True, default='active')
    change_church = fields.Char(string='Change Church')
    date_death = fields.Date(string='Date of Death')
    church_transfer_date = fields.Date(string='Church Transfer Date')
    church_move_out_date = fields.Date(string='Church Move Out Date')

    def _compute_age(self):
        for record in self:
            if record.date_birthday:
                dt = record.date_birthday
                d2 = date.today()
                rd = relativedelta(d2, dt)
                record.age = rd.years
