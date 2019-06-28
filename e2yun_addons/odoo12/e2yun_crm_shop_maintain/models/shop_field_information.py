# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CrmTeamADDinformation(models.Model):
    _inherit = ['crm.team']

    shop_type = fields.Char('门店类别')
    shop_code = fields.Char('门店编码')
    sales_organization = fields.Char('销售组织')
    sales_organization_name = fields.Char('销售组织名称')
    sales_channel = fields.Char('分销渠道名称')
    sales_office = fields.Char('销售办公室')
    sales_office_description = fields.Char('销售办公室描述')
    address = fields.Char('详细地址')
    tel = fields.Char('联系电话')

    street = fields.Char('地址')
    street2 = fields.Char('地址2')
    zip = fields.Char('邮编', change_default=True)
    city = fields.Char('市')
    state_id = fields.Many2one("res.country.state", string='省', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='国家', ondelete='restrict')

class ResUsers(models.Model):
    _inherit = 'res.users'

    member_type = fields.Selection([
        ('manager', '店长'),
        ('sales', '导购'),
        ('designer', '设计师')], string='成员类别', default='sales')
