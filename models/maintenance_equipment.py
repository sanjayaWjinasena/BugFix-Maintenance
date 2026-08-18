# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    x_studio_electricity = fields.Float(string='Electricity')
    x_studio_lubricant = fields.Float(string='Lubricant')
    x_studio_water = fields.Float(string='Water')
