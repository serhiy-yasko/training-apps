from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate advertisement"

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    date_availability = fields.Date(
        'Available From', copy=False,
        default=fields.Date.to_date(
            f"{fields.Date.today().year}-{fields.Date.today().month+3}-{fields.Date.today().day}"))
    postcode = fields.Char('Postcode')
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation')
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('cancelled', 'Cancelled')], default='new')
