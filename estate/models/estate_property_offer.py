from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offer for a real estate property"
    _order = "price desc"

    price = fields.Float('Price')
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    property_type_id = fields.Many2one(related='property_id.property_type_id', string="Property Type", store=True)
    validity = fields.Integer('Validity (days)', default=7)
    date_deadline = fields.Date('Deadline', compute='_compute_deadline', inverse="_inverse_deadline")

    @api.model_create_multi
    def create(self, vals):
        if vals[0]['price'] < self.env['estate.property'].browse(vals[0]['property_id']).best_price:
            raise UserError("An offer with a higher price already exists")

        self.env['estate.property'].browse(vals[0]['property_id']).state = 'offer_received'
        return super().create(vals)

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price < 1:
                raise ValidationError("The offer price must be strictly positive")

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
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = 'offer_accepted'
        return True

    def action_refuse(self):
        for record in self:
            record.status = 'refused'
            record.property_id.state = 'offer_received'
        return True
