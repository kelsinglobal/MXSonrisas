# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class AreasAttention(models.Model):
    _name = 'medical.areas.attention'
    _description = 'Areas attention'

    name = fields.Char('Name', required=True)
    medical_center_id = fields.Many2one('patient.affiliation', 'Medical center', required=True)
    allows_reservation = fields.Boolean('Allows reservation')
    state = fields.Selection(string='Status',
                             selection=[('assigned', 'Assigned'), ('available', 'Available'),
                                        ('out_service', 'Out of service')])
    operating_rooms = fields.Boolean('Its operating rooms')






























