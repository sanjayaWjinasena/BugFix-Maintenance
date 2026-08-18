# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceEquipmentCategory(models.Model):
    _inherit = 'maintenance.equipment.category'

    x_studio_journal_type = fields.Many2one('x_journal_types', string='Journal Type')
