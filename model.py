# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError


class ThiCong(models.Model):
    _name = 'thi.cong'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'name'
    _order = 'id desc'
    _description = 'Thi công công trình'

    name = fields.Char(string='',track_visibility = 'onchange')
    state = fields.Selection([('0','new'),('1','confirm')],string='')
