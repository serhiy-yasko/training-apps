from odoo import api, fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of a real estate property"
    _order = "sequence,name"

    name = fields.Char('Title', required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")
    sequence = fields.Integer('Sequence', default=1, help="Used to manually order property types.")
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id', string="Offers")
    offer_count = fields.Integer('Offer Count', compute='_compute_offer_count')

    _sql_constraints = [(
        'unique_name',
        'UNIQUE(name)',
        'The name must be unique',
    )]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
