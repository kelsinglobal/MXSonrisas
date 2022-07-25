# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.model
    def _default_alarms(self):
        alarms = self.env['calendar.alarm'].search([('alarm_type', '=', 'sms'), ('duration', '=', 1),
                                                    ('interval', 'in', ['hours', 'days'])], limit=2)
        return alarms

    medical_center_id = fields.Many2one('patient.affiliation', 'Medical center')
    area_attention_id = fields.Many2one('medical.areas.attention', 'Area attention')
    doctor_id = fields.Many2one('hr.employee', 'Doctor', domain="[('is_medical_personnel','=',True)]")
    line_ids = fields.One2many('calendar.event.line', 'calendar_id', 'Line service')
    alarm_ids = fields.Many2many(
        'calendar.alarm', 'calendar_alarm_calendar_event_rel',
        string='Reminders', ondelete="restrict", default=_default_alarms,
        help="Notifications sent to all attendees to remind of the meeting.")


class CalendarEventLine(models.Model):
    _name = 'calendar.event.line'
    _description = 'Calendar event line service'

    calendar_id = fields.Many2one('calendar.event', 'Calendar')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    quantity = fields.Float('Quantity', default=1)
    price = fields.Float('Price')
