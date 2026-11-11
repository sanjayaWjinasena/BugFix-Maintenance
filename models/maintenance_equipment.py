from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    electricity = fields.Float()
    lubricant = fields.Float()
    water = fields.Float()
