from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    electricity = fields.Float(string="Electricity")
    lubricant = fields.Float(string="Lubricant")
    water = fields.Float(string="Water")
