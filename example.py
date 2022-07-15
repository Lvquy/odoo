
# ./odoo-bin -c odoo.conf -d database_name -u module_name
class SamPlace(models.Model):
    def notification(self):
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': ('Thông báo'),
                'message': 'Chưa có tài khoản liên kết hệ thống',
                'type': 'warning',  # types: success,warning,danger,info
                'next': {'type': 'ir.actions.act_window_close'},
                'sticky': False,  # True/False will display for few seconds if false
            },
        }
        return notification

    def open_form(self):
        return {
            'name': ('Cài đặt giá cho sản phẩm'),
            'type': 'ir.actions.act_window',
            'res_model': 'set.price',
            'view_mode': 'form',
            'target': 'new',
        }

    discount = int(self.env['ir.config_parameter'].sudo().get_param('custom_b2c.discount'))
    # return type = string
    force_save = "1"  # nếu cảm thấy khó khăn quá trong việc lưu filed trong database

    """
    <div class="alert alert-info text-center o_form_header" role="alert">
        <a class="close" data-dismiss="alert" href="#">x</a>
        <div>
            <strong>Today is birthday!</strong>
        </div>
    </div>

------------ cho phep google email truy cap may he thong
        https://accounts.google.com/b/0/DisplayUnlockCaptcha
        
         <record id="crm_rule_personal_lead" model="ir.rule">
        <field name="name">Personal Leads</field>
        <field ref="model_crm_lead" name="model_id"/>
        <field name="domain_force">['|',('user_id','=',user.id),('user_id','=',False)]</field>
        <field name="groups" eval="[(4, ref('sales_team.group_sale_salesman'))]"/>
    </record>

    <record id="group_sale_salesman" model="res.groups">
            <field name="name">User: Own Documents Only</field>
            <field name="category_id" ref="base.module_category_sales_sales"/>
            <field name="implied_ids" eval="[(4, ref('base.group_user'))]"/>
            <field name="comment">the user will have access to his own data in the sales application.</field>
        </record>


(0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
(1, ID, { values }) -- update the linked record with id = ID (write values on it)
(2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
(3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
(4, ID) -- link to existing record with id = ID (adds a relationship)
(5) -- unlink all (like using (3,ID) for all linked records)
(6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)

-------------
    """
