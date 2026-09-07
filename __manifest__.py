# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Maintenance',
    'version': '17.0.0.0.6',
    'summary': 'Studio-to-Python port for BugFix-Maintenance',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Human Resources/Maintenance',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v17.0.0.0.6: close remaining Maintenance gap via cross-module audit.
    #   Server actions:  0 shipped -> 12 shipped (100% effective)
    #     MR/MNT_REQ maintenance workflow: planning / in-progress /
    #     repaired / scraped + MR create from maintenance request.
    #   Base.automations: 0 -> 1 (Update Cost Per Hour in Work Center)
    #   Window actions:  0 -> 1 (Maintenance Requests look-alike)
    #   Views:           0 -> 5 shipped (2 form + 1 tree on maintenance
    #     .request/.equipment.category/.stage; 6 xpaths pre-flight-dropped)
    #   Fields:          0 gap
    # Also renamed to 'Jinasena : Module : Maintenance' + added shared
    # icon at static/description/icon.png.
    'depends': ['base_setup', 'maintenance'],
    'data': [
        'data/server_actions.xml',
        'data/server_actions_v2.xml',
        'data/automations.xml',
        'data/automations_v2.xml',
        'data/window_actions.xml',
        'views/maintenance_equipment_category_studio_ported.xml',
        'views/maintenance_request_studio_ported.xml',
        'views/maintenance_equipment_studio_ported.xml',
        'views/maintenance_stage_studio_ported.xml',
        'views/studio_ported_5_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}