from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of a real estate property"
    _order = "name"

    name = fields.Char('Title', required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")

    _sql_constraints = [(
        'unique_name',
        'UNIQUE(name)',
        'The name must be unique',
    )]
