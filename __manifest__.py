# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Maintenance',
    'version': '17.0.0.0.11',
    'summary': 'Studio-to-Python port for BugFix-Maintenance',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Human Resources/Maintenance',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v17.0.0.0.8: hotfix v17.0.0.0.7 - add mrp_maintenance dep.
    # v17.0.0.0.7 crashed on view 3254 with:
    #   Element '<xpath expr="//field[@name='production_id']">' cannot
    #   be located in parent view
    # Root cause: production_id is added to maintenance.request by
    # mrp_maintenance module (its view #5490 inherits our parent
    # view #627 with priority 16). At view application time both
    # views should sort by priority - our v99 loads after
    # mrp_maintenance v16 - so composed arch SHOULD have production_id.
    # BUT: mrp_maintenance and BugFix-Maintenance are PEER modules
    # (no dep either way). Module load order among peers is arbitrary,
    # usually alphabetical. BugFix-Maintenance sorts before
    # mrp_maintenance ('B' < 'm'), so at our load time mrp_maintenance's
    # view 5490 doesn't exist yet - can't apply, production_id not
    # in composed arch.
    # Fix: add 'mrp_maintenance' to depends so it loads before us.
    # v17.0.0.0.7: hotfix v17.0.0.0.6 - add base_automation dep.
    # v17.0.0.0.6 crashed with:
    #   ValueError: Wrong value for ir.actions.server.usage: 'base_automation'
    # Root cause: server_action_1566_mnt_code_gen (from existing
    # data/server_actions.xml) uses usage='base_automation'. That
    # selection value is provided by the base_automation module -
    # NOT by base or maintenance. Our v0.0.6 shipped 12 new server
    # actions many of which also use usage='base_automation', which
    # triggered Odoo to re-write ALL server actions on the module,
    # revalidating the OLD one against the current selection set.
    # At Maintenance load-time, base_automation module isn't in our
    # transitive deps chain so the selection value isn't yet
    # available.
    # Fix: add 'base_automation' to depends.
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
    'depends': ['base_setup', 'maintenance', 'base_automation', 'mrp_maintenance'],
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
        'data/server_actions_gap.xml',
        'data/ir_defaults_gap.xml',
        'views/maintenance_equipment_e_views.xml',
        'views/maintenance_request_e_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}