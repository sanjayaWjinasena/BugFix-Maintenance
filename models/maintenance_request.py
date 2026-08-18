# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    x_studio_diagnosis_details = fields.Text(string='Diagnosis Details')
    x_studio_float_field_hmeW9 = fields.Float(string='New Decimal')
    x_studio_integer_field_1Zbhs = fields.Integer(string='New Integer')
    x_studio_journal_type_1 = fields.Many2one('x_journal_types', string='Journal Type', readonly=True)
    x_x_studio_maintenance_request___stock_picking_count = fields.Integer(string='Maintenance Request # count', store=False)
    x_x_studio_many2one_field_THFu6__x_material_request_count = fields.Integer(string='MR', store=False)
