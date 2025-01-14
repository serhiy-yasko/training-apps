from odoo import fields, models


class RecurringPlan(models.Model):
    _name = "estate.property"
    _description = "Real estate advertisement"
    _order = "sequence"

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    date_availability = fields.Date('Availability Date')
    postcode = fields.Char('Postcode')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area (sqm)')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation')
