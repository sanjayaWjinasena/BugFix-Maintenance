# BugFix-Maintenance — views to hand-port

8 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 3771 | activity | `maintenance.request` | Default activity view for ir.model(689,) | — |
| 2 | 5333 | form | `maintenance.equipment.category` | Odoo Studio: equipment.category.form customization | equipment.category.form |
| 3 | 5332 | tree | `maintenance.equipment.category` | Odoo Studio: equipment.category.tree customization | equipment.category.tree |
| 4 | 5495 | form | `maintenance.equipment` | Odoo Studio: equipment.form customization | equipment.form |
| 5 | 3254 | form | `maintenance.request` | Odoo Studio: equipment.request.form customization | equipment.request.form |
| 6 | 5318 | tree | `maintenance.request` | Odoo Studio: equipment.request.tree customization | equipment.request.tree |
| 7 | 5071 | tree | `maintenance.stage` | Odoo Studio: equipment.stage.tree customization | equipment.stage.tree |
| 8 | 5072 | form | `maintenance.request` | equipment.request.form_Button | equipment.request.form |
