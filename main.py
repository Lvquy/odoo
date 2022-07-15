# Odoo 15 Sample
utf8 = """# -*- coding: utf-8 -*-


"""
module_name = "vitinhso" # ex: b2c_mart
class_name = "NhanSu" # ex. ProductTemplate
model_id = "nhan.su" #ex: product.template
desc = "Nhân sự" #ex: Product Template
model_form_tree = model_id.replace('.', '_') # is: product_template
tree_form_string = "Nhân sự" # ex: Product Template

a = """
from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError"""
models = """class %s(models.Model):
    _name = '%s'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'name'
    _order = 'id desc'
    _description = '%s'

    name = fields.Char(string='',track_visibility = 'onchange')
    state = fields.Selection([('0','new'),('1','confirm')],string='')
""" %(class_name, model_id, desc)

with open("model.py", "r+") as f:
    f.truncate()  # remove all line
    f.seek(0)  # rewind
    f.write(utf8 + a + "\n" + models)  # write the new line before

# ---------- manifest ---------
manifest = """
{
    'name': '%s',
    'version': '1',
    'category': 'category_xxx',
    'live_test_url': 'live_test_url_xxx',
    'summary': 'summary_xxx',
    'author': 'author_xxx',
    'company': 'company_xxx',
    'website': 'website_xxx',
    'depends': 'depends_xxx',
    'data': [
        'data/sequence.xml',
        # security
        'security/module_name_groups.xml',
        'security/ir.model.access.csv',

        # views
        'views/xxx.xml',

        # report
        'report/xxx.xml',

    ],
    'assets': {
        'web.assets_backend': [],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
}
""" % class_name

with open("__manifest__.py", "r+") as f:
    f.truncate()  # remove all line
    f.seek(0)
    f.write(utf8 + manifest + "\n")

# -------------- views


views = """
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <record id="%s_form" model="ir.ui.view">
            <field name="name">%s.form</field>
            <field name="model">%s</field>
            <field name="arch" type="xml">
                <form string="%s">
                    <header>
                            <field name="state" widget="statusbar" statusbar_visible="0,1"/>
                            <button name="confirm" string="Confirm" type="object" attrs="{'invisible':[('state', 'in', ('1'))]}"/>
                        </header>
                    <sheet>
                        <group string="">
                            <group>
                                <field name="" attrs="{
                                'invisible':[('state', 'in', ('2','3'))],
                                'readonly':[('state', 'in', ('1'))]}"/>
                            </group>
                        </group>
                        <notebook>
                            <page name="page_name" string="page string">
                            </page>
                        </notebook>
                    </sheet>
                    <div class="oe_chatter">
                        <field name="message_follower_ids"/>
                        <field name="activity_ids"/>
                        <field name="message_ids"/>
                    </div>
                </form>
            </field>
        </record>

        <record id="%s_tree" model="ir.ui.view">
            <field name="name">%s.tree</field>
            <field name="model">%s</field>
            <field name="arch" type="xml">
                <tree string="%s" editable="bottom" decoration-danger="state=='0'" decoration-success="state=='1'">
                    <field name="name" optional="show"/>
                </tree>
            </field>
        </record>

        <!-- action view-->
        <record id="action_view_%s" model="ir.actions.act_window">
            <field name="name">%s</field>
            <field name="res_model">%s</field>
            <field name="view_mode">tree,form</field>
            <field name="domain">[('create_uid', '=', uid)]</field>
            <field name="help" type="html">
                <p class="o_view_nocontent_smiling_face">
                    Create a new ...
                </p>
            </field>
        </record>
        <menuitem id="menu_%s" name="%s" sequence="1"
              web_icon="%s,static/src/img/logo.png" groups="base.group_system"/>
        <menuitem id="menu_sub_%s" name="%s" parent="menu_%s" action="action_view_%s"
              sequence="1" groups="base.group_system"/>
    </data>
</odoo>
""" % (model_form_tree, model_id, model_id, tree_form_string, model_form_tree, model_id, model_id, tree_form_string,
       model_form_tree, tree_form_string, model_id, model_form_tree, tree_form_string,module_name, model_form_tree, tree_form_string,
       model_form_tree, model_form_tree)
with open("views.xml", "r+") as f:
    f.truncate()
    f.seek(0)
    f.write(views + "\n")

# ------- search ----------
search = """
<?xml version="1.0" encoding="utf-8"?>
<odoo>
<!--search-->
    <record id="view_search_%s" model="ir.ui.view">
        <field name="name">%s.search</field>
        <field name="model">%s</field>
        <field name="priority" eval="15"/>
        <field name="arch" type="xml">
            <search string="Search %s">
                <field name="name"/>
                <field name="state"/>
                <filter string="Done" name="done" domain="[('state','=','1')]"/>
                <filter string="Draft" name="draft" domain="[('state','=','0')]"/>
                <group expand="0" string="Group By">
                    <filter string="Trạng thái" name="state" domain="[]" context="{'group_by': 'state'}"/>
                </group>
            </search>
        </field>
    </record>
</odoo>
""" %(model_form_tree,model_id,model_id,tree_form_string)
with open("search.xml", "r+") as f:
    f.truncate()
    f.seek(0)
    f.write(search + "\n")
access = """
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink

access_%s_%s_root,%s.root,model_%s,base.group_system,1,1,1,1
""" %(module_name,model_form_tree,model_id,model_form_tree)
with open("ir.model.access.csv", "r+") as f:
    f.truncate()
    f.seek(0)
    f.write(access + "\n")
    f.closed
# ------------ groups --------------
gr = """
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <record model="ir.module.category" id="module_%s_user">
            <field name="name">%s Group</field>
            <field name="description">%s Group</field>
            <field name="sequence">30</field>
        </record>
        <record id="%s.group_%s" model="res.groups">
            <field name="name">%s Group</field>
            <field name="category_id" ref="%s.module_%s_user"/>
        </record>
    </data>
</odoo>
""" %(module_name,module_name,module_name,module_name,module_name,module_name,module_name,module_name)
with open("groups.xml", "r+") as f:
    f.truncate()
    f.seek(0)
    f.write(gr + "\n")
print("Success!")
