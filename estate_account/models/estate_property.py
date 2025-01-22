from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = ["estate.property"]

    def action_mark_sold(self):
        current_property = self.env['estate.property'].search([], order='id desc', limit=1)
        administrative_fee = 100.0
        values = {
            'partner_id': current_property.buyer_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    'name': current_property.name,
                    'quantity': 1.0,
                    'price_unit': current_property.selling_price * 0.06 + administrative_fee,
                })
            ],
        }
        self.env['account.move'].create(values)
        return super().action_mark_sold()
