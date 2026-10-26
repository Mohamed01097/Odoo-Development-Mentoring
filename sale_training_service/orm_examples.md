# Run Sell

./odoo-bin shell -c ./odoo.conf -d odoo_dev_mentoring
2026-10-26 11:06:55,680 36242 WARNING ? odoo.tools.config: missing --http-interface/http_interface, using 0.0.0.0 by default, will change to 127.0.0.1 in 20.0 
2026-10-26 11:06:55,680 36242 INFO ? odoo: Odoo version 19.0 
2026-10-26 11:06:55,680 36242 INFO ? odoo: Using configuration file at /home/islam/odoo-folds/odoo19/odoo-19/odoo.conf 
2026-10-26 11:06:55,680 36242 INFO ? odoo: addons paths: _NamespacePath(['/home/islam/odoo-folds/odoo19/odoo-19/odoo/addons', '/home/islam/.local/share/Odoo/addons/19.0', '/home/islam/odoo-folds/odoo19/odoo-19/addons', '/home/islam/odoo-folds/odoo19/odoo-19/custom_addons', '/home/islam/odoo-folds/odoo19/odoo-19/Odoo-Development-Mentoring']) 
2026-10-26 11:06:55,681 36242 INFO ? odoo: database: odoo19@localhost:5432 
2026-10-26 11:06:56,010 36242 INFO ? odoo.service.server: Initiating shutdown 
2026-10-26 11:06:56,010 36242 INFO ? odoo.service.server: Hit CTRL-C again or send a second signal to force the shutdown. 
2026-10-26 11:06:56,056 36242 INFO odoo_dev_mentoring odoo.modules.loading: loading 1 modules... 
2026-10-26 11:06:56,062 36242 INFO odoo_dev_mentoring odoo.modules.loading: 1 modules loaded in 0.01s, 0 queries (+0 extra) 
2026-10-26 11:06:56,064 36242 WARNING odoo_dev_mentoring odoo.modules.module: Missing `author` key in manifest for 'sale_training_service', defaulting to '' 
2026-10-26 11:06:56,085 36242 INFO odoo_dev_mentoring odoo.modules.loading: loading 62 modules... 
2026-10-26 11:06:56,556 36242 WARNING odoo_dev_mentoring odoo.registry: Model attribute '_sql_constraints' is no longer supported, please define models.Constraint on the model. 
2026-10-26 11:06:56,556 36242 INFO odoo_dev_mentoring odoo.modules.loading: 62 modules loaded in 0.47s, 0 queries (+0 extra) 
2026-10-26 11:06:56,728 36242 INFO odoo_dev_mentoring odoo.modules.loading: Modules loaded. 
2026-10-26 11:06:56,770 36242 INFO odoo_dev_mentoring odoo.registry: Registry loaded in 0.747s 
env: <odoo.orm.environments.Environment object at 0x74c1da763dd0>
odoo: <module 'odoo' (<_frozen_importlib_external.NamespaceLoader object at 0x74c1e2712710>)>
openerp: <module 'odoo' (<_frozen_importlib_external.NamespaceLoader object at 0x74c1e2712710>)>
self: res.users(1,)


# ENV Object
openerp: <module 'odoo' (<_frozen_importlib_external.NamespaceLoader object at 0x7e4b10f12750>)>
self: res.users(1,)
>>> order = env['sale.order']
>>> order
sale.order()
>>> order.action_about_env()
{'user_id': 1, 'user': res.users(1,), 'user_name': 'OdooBot', 'company_id': 1, 'context': {'lang': 'en_US', 'tz': 'Europe/Brussels', 'uid': 1}}
>>> order.action_about_orders_info()
sale.order(16, 14, 13, 12, 10, 8, 7, 6, 4, 3, 9, 15, 11, 17, 20, 19, 5, 2, 1, 18)
>>> 


# Orders Info

self: res.users(1,)
>>> orders = env['sale.order']
>>> orders.action_about_orders_info()
{'model_name': 'sale.order', 'orders_num': 20, 'orders': sale.order(16, 14, 13, 12, 10, 8, 7, 6, 4, 3, 9, 15, 11, 17, 20, 19, 5, 2, 1, 18), 'orders_ids': [16, 14, 13, 12, 10, 8, 7, 6, 4, 3, 9, 15, 11, 17, 20, 19, 5, 2, 1, 18]}
>>> 

### --------------------------------
>>> orders = env["sale.order"].search([])
>>> 
>>> print(orders._name)
sale.order
>>> print(len(orders))
20
>>> print(orders.ids)
[16, 14, 13, 12, 10, 8, 7, 6, 4, 3, 9, 15, 11, 17, 20, 19, 5, 2, 1, 18]
>>> 
>>> print(env.user)
res.users(1,)
>>> print(env.company)
res.company(1,)
>>> 


# Search - Browse - Browse +Exists

>>> orders = env["sale.order"].search([
...     ("state", "=", "draft"),
... ])
>>> orders
sale.order(3, 5, 2, 1)
>>> order = env["sale.order"].browse(10)
>>> order
sale.order(10,)
>>> order = env["sale.order"].browse(999999)
>>> 
>>> print(bool(order))
True
>>> print(order.exists())
sale.order()
>>> order = env["sale.order"].browse(999999)
>>> 
>>> order
sale.order(999999,)
>>> 


# Domains 
>>> orders = env["sale.order"].search([
...     ("state", "in", ["draft", "sent"]),
...     ("amount_total", ">=", 2000),
...     ("amount_total", "<=", 5000),
... ])
>>> orders
sale.order(2,)

>>> domain = ['|', ('state','=', 'sent'), ('amount_total', '>', 1000)]
>>> orders = env['sale.order'].search(domain)
>>> orders
sale.order(16, 14, 7, 4, 3, 15, 11, 20, 19, 2, 1)
>>> 

# Sorted - Mapped - Filtered 

>>> orders = env["sale.order"].search([])
>>> 
>>> high_value_orders = orders.filtered(
...     lambda order: order.amount_total > 5000
... )
>>> high_value_orders
sale.order(3,)
>>> partners = orders.mapped("partner_id")
>>> partners
res.partner(10, 16, 11, 7, 9)
>>> partner_names = orders.mapped("partner_id.name")
>>> partner_names
['Gemini Furniture', 'Lumber Inc', 'Ready Mat', 'Joel Willis', 'Acme Corporation']
>>> sorted_orders = orders.sorted(
...     key=lambda order: order.amount_total,
...     reverse=True,
... )
>>> sorted_orders
sale.order(3, 20, 2, 4, 19, 1, 7, 14, 15, 16, 11, 17, 18, 10, 6, 9, 12, 8, 13, 5)
>>> 


>>> partner = env['res.partner'].create({'name': 'Islam'})
>>> partner
res.partner(43,)
>>> 





