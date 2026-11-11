from odoo import fields, models


class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    diagnosis_details = fields.Text()
    float_field_hmeW9 = fields.Float(string="New Decimal")
    integer_field_1Zbhs = fields.Integer(string="New Integer")
    journal_type_1 = fields.Many2one(
        "journal_types", string="Journal Type", readonly=True
    )
    maintenance_request___stock_picking_count = fields.Integer(
        string="Maintenance Request # count", store=False
    )
    many2one_field_THFu6__x_material_request_count = fields.Integer(
        string="MR", store=False
    )
