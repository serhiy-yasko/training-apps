from datetime import timedelta
from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offer for a real estate property"

    price = fields.Float('Price')
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    validity = fields.Integer('Validity (days)', default=7)
    date_deadline = fields.Date('Deadline', compute='_compute_deadline', inverse="_inverse_deadline")

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days
            record.create_date = record.date_deadline - timedelta(days=record.validity)

    def action_accept(self):
        for record in self:
            record.status = 'accepted'
        return True

    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
