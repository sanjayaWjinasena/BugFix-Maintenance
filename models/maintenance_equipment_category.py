from odoo import fields, models


class MaintenanceEquipmentCategory(models.Model):
    _inherit = "maintenance.equipment.category"

    journal_type = fields.Many2one("journal_types", string="Journal Type")
