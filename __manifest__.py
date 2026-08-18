# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Maintenance',
    'version': '17.0.0.0.2',
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
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}