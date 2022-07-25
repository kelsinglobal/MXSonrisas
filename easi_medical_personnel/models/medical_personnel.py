# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class MedicalSpecialty(models.Model):
    _name = 'medical.specialty'
    _description = 'medical specialty'

    key = fields.Char("Key")
    name = fields.Char("Name")


class MedicalInstitution(models.Model):
    _name = 'medical.institution'
    _description = 'medical institution'

    key = fields.Char("Key")
    name = fields.Char("Name")


class MedicalFaculty(models.Model):
    _name = 'medical.faculty'
    _description = 'medical faculty'

    key = fields.Char("Key")
    name = fields.Char("Name")


class EmployeeCategory(models.Model):
    _name = 'employee.category'
    _description = 'employee category'

    name = fields.Char("Name")


class EmployeeProfession(models.Model):
    _name = 'employee.profession'
    _description = 'employee profession'

    key = fields.Char("Key")
    name = fields.Char("Name")


class MedicalPersonnel(models.Model):
    _name = 'hr.employee'
    _inherit = ['hr.employee']

    is_medical_personnel = fields.Boolean("Is a medical Personnel")
    name_copy = fields.Char(string="Employee Name Copy", compute='_compute_name_copy', store=True)
    father_lastname = fields.Char("Father Lastname")
    mother_lastname = fields.Char("Mother Lastname")
    employee_name = fields.Char("Name")
    group_rh = fields.Selection([('unknown', 'Unknown'),
                                 ('a+', 'A+'),
                                 ('b+', 'B+'),
                                 ('ab+', 'AB+'),
                                 ('o+', 'O+'),
                                 ('a-', 'A-'),
                                 ('b-', 'B-'),
                                 ('ab-', 'AB-'),
                                 ('o-', 'O-')], string="Group and Rh")
    profession = fields.Many2one('employee.profession', "Profession", ondelete='cascade')
    professional_dni = fields.Char("Professional DNI")
    medical_institution = fields.Many2one('medical.institution', "Institution", ondelete='cascade')
    employee_category = fields.Many2one('employee.category', "Employee Category", ondelete='cascade')
    hr_employee_line_ids = fields.One2many('hr.employee.line', 'employee_id', "Specialties")

    @api.model
    def create(self, vals):
        employee = super(MedicalPersonnel, self).create(vals)
        if employee.father_lastname and employee.employee_name:
            values = [employee.father_lastname, employee.employee_name]
            if employee.mother_lastname:
                values.insert(1, employee.mother_lastname)
            employee.name = ' '.join(values)
        return employee

    @api.depends('name')
    def _compute_name_copy(self):
        for employee in self:
            employee.name_copy = employee.name

    @api.onchange('father_lastname', 'mother_lastname', 'employee_name')
    def _onchange_names(self):
        if self.father_lastname and self.employee_name:
            values = [self.father_lastname, self.employee_name]
            if self.mother_lastname:
                values.insert(1, self.mother_lastname)
            self.name = ' '.join(values)


class HREmployeeLine(models.Model):
    _name = 'hr.employee.line'
    _description = 'hr employee line'

    medical_specialty = fields.Many2one('medical.specialty', "Specialty", ondelete='cascade')
    medical_faculty = fields.Many2one('medical.faculty', "Faculty", ondelete='cascade')
    dni = fields.Char("DNI")
    validity = fields.Date("Validity")
    employee_id = fields.Many2one('hr.employee', "Medical Personnel", ondelete='cascade')


