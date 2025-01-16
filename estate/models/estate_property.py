from odoo import api, fields, models


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
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    salesperson_id = fields.Many2one(
        'res.users', string="Salesperson", default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    total_area = fields.Integer('Total Area (sqm)', compute='_compute_total_area')
    best_price = fields.Float('Best Offer', compute='_compute_best_price')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.mapped('offer_ids.price'), default=0.0)
