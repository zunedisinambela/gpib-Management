from odoo import api, fields, models


class FamilyMaster(models.Model):
    _name = "gpib.family"
    _description = "Family Master"

    name = fields.Char(string='Name', required=True)
    qty = fields.Integer(string='Qty')
    address = fields.Text(string='Address', required=True)
    sector_id = fields.Many2one('gpib.sector', string='Name Sector', required=True)
    line_ids = fields.One2many('gpib.family.line', 'family_id')


class FamilyLine(models.Model):
    _name = "gpib.family.line"
    _description = "Family Line"

    family_id = fields.Many2one(string='Family Name', required=True)
    name = fields.Char(string='Name', required=True)
    date_birthday = fields.Date(string='Date of Birth', required=True)
    date_baptism = fields.Date(string='Date of Baptis')
    date_sidi = fields.Date(string='Date of Sidi')
    last_education = fields.Char(string='Last Education')
    pelkat_id = fields.Many2one(string='Pelkat', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True)
    position = fields.Char(string='Position', required=True)
    wedding_date = fields.Date(string='Wedding Date')
    state_married = fields.Selection([
        ('married', 'Married'),
        ('not_married', 'Not Married Yet'),
        ('divorced', 'Divorced'),
        ('death_divorce', 'Death Divorce')
    ], required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('not_active', 'Not Active'),
        ('die', 'Die')
    ], required=True)
    change_church = fields.Char(string='Change Church')
    date_death = fields.Date(string='Date of Death')
    church_transfer_date = fields.Date(string='Church Transfer Date')
    church_move_out_date = fields.Date(string='Church Move Out Date')
