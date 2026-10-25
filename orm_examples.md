vboxuser@ubuntu-VM:~/PycharmProjects/Odoo-Development-Mentoring$ git bransh
git: 'bransh' is not a git command. See 'git --help'.

The most similar command is
        branch
vboxuser@ubuntu-VM:~/PycharmProjects/Odoo-Development-Mentoring$  /home/vboxuser/odoo-venv/bin/python3 /home/vboxuser/odoo/odoo-bin shell -c /home/vboxuser/odoo/debian/odoo.conf -d odoo19
2026-10-25 18:53:13,362 11012 WARNING ? odoo.tools.config: option db_host reads 'False' in the config file at /home/vboxuser/odoo/debian/odoo.conf but isn't a boolean option, skip 
2026-10-25 18:53:13,362 11012 WARNING ? odoo.tools.config: option db_port reads 'False' in the config file at /home/vboxuser/odoo/debian/odoo.conf but isn't a boolean option, skip 
2026-10-25 18:53:13,362 11012 WARNING ? odoo.tools.config: option db_password reads 'False' in the config file at /home/vboxuser/odoo/debian/odoo.conf but isn't a boolean option, skip 
2026-10-25 18:53:13,362 11012 WARNING ? odoo.tools.config: missing --http-interface/http_interface, using 0.0.0.0 by default, will change to 127.0.0.1 in 20.0 
2026-10-25 18:53:13,363 11012 INFO ? odoo: Odoo version 19.0 
2026-10-25 18:53:13,363 11012 INFO ? odoo: Using configuration file at /home/vboxuser/odoo/debian/odoo.conf 
2026-10-25 18:53:13,363 11012 INFO ? odoo: addons paths: _NamespacePath(['/home/vboxuser/odoo/odoo/addons', '/home/vboxuser/.local/share/Odoo/addons/19.0', '/home/vboxuser/odoo/addons', '/home/vboxuser/PycharmProjects/Odoo-Development-Mentoring']) 
2026-10-25 18:53:13,364 11012 INFO ? odoo: database: vboxuser@default:default 
2026-10-25 18:53:14,183 11012 INFO ? odoo.service.server: Initiating shutdown 
2026-10-25 18:53:14,183 11012 INFO ? odoo.service.server: Hit CTRL-C again or send a second signal to force the shutdown. 
2026-10-25 18:53:14,205 11012 INFO odoo19 odoo.modules.loading: loading 1 modules... 
2026-10-25 18:53:14,210 11012 INFO odoo19 odoo.modules.loading: 1 modules loaded in 0.01s, 0 queries (+0 extra) 
2026-10-25 18:53:14,213 11012 WARNING odoo19 odoo.modules.module: Missing `license` key in manifest for 'edit_sale', defaulting to LGPL-3 
2026-10-25 18:53:14,222 11012 WARNING odoo19 odoo.modules.module: Missing `license` key in manifest for 'sale_risk_management', defaulting to LGPL-3 
2026-10-25 18:53:14,226 11012 WARNING odoo19 odoo.modules.module: Missing `license` key in manifest for 'sale_order_approval', defaulting to LGPL-3 
2026-10-25 18:53:14,231 11012 INFO odoo19 odoo.modules.loading: loading 59 modules... 
2026-10-25 18:53:15,190 11012 INFO odoo19 odoo.modules.loading: 59 modules loaded in 0.96s, 0 queries (+0 extra) 
2026-10-25 18:53:15,403 11012 INFO odoo19 odoo.tools.version_tag_reset: Detected tp_versions_used at offset 410, reset enabled 
2026-10-25 18:53:15,408 11012 INFO odoo19 odoo.modules.loading: Modules loaded. 
2026-10-25 18:53:15,488 11012 INFO odoo19 odoo.registry: Registry loaded in 1.300s 
env: <odoo.orm.environments.Environment object at 0x7d9db50df360>
odoo: <module 'odoo' (namespace) from ['/home/vboxuser/odoo/odoo']>
openerp: <module 'odoo' (namespace) from ['/home/vboxuser/odoo/odoo']>
self: res.users(1,)
>>> order=self.env['sale.order'].search()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: BaseModel.search() missing 1 required positional argument: 'domain'
>>> orders = env['sale.order'].search([])
>>> orders
sale.order(24, 13, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2)
>>> orders = env['sale.order'].search([],limit=5)
>>> orders
sale.order(24, 13, 23, 22, 21)
>>> orders._name
'sale.order'
>>> orders.ids
[24, 13, 23, 22, 21]
>>> len(orders)
5
>>> env.user
res.users(1,)
>>> env.company
res.company(1,)
>>> self.env [] 