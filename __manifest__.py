# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Maintenance',
    'version': '17.0.0.0.5',
    'summary': 'Studio-to-Python port for BugFix-Maintenance',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Human Resources/Maintenance',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    'depends': ['base_setup', 'maintenance'],
    'data': [
        'data/server_actions.xml',
        'data/automations.xml',
        'views/maintenance_equipment_category_studio_ported.xml',
        'views/maintenance_request_studio_ported.xml',
        'views/maintenance_equipment_studio_ported.xml',
        'views/maintenance_stage_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}