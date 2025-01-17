from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of a real estate property"

    name = fields.Char('Title', required=True)

    _sql_constraints = [(
        'unique_name',
        'UNIQUE(name)',
        'The name must be unique',
    )]
