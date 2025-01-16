from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag of a real estate property"

    name = fields.Char('Title', required=True)
