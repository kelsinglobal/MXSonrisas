# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class PatientAffiliation(models.Model):
    _name = 'patient.affiliation'
    _description = 'Patient affiliation'

    name = fields.Char('Name', required=True)






























