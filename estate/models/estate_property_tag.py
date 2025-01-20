from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag of a real estate property"
    _order = "name"

    name = fields.Char('Title', required=True)
    colour = fields.Integer('Colour')

    _sql_constraints = [(
        'unique_name',
        'UNIQUE(name)',
        'The name must be unique',
    )]
