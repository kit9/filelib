# Copyright 2017-2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import os
from os.path import join as opj

from odoo import api, fields, models, tools


class account_analytic_line(models.Model):
    _name = "account.analytic.line"
    _inherit = "account.analytic.line"

    milestone = fields.Many2one("project.milestone", '里程碑', domain="[('project_id','=',project_id)]")
    state = fields.Selection([('draft', '草稿'), ('posted', '过账')], string='状态',
                             required=True, copy=False, default='draft',
                             help='All manually created new journal entries are usually in the status \'Unposted\', '
                                  'but you can set the option to skip that status on the related journal. '
                                  'In that case, they will behave as journal entries automatically created by the '
                                  'system on document validation (invoices, bank statements...) and will be created '
                                  'in \'Posted\' status.')


class MisCommittedPurchase(models.Model):
    _name = "mis.analytic"
    _description = "MIS Analytic"
    _auto = False

    line_type = fields.Char()
    name = fields.Char()
    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account", string="Analytic Account"
    )
    account_id = fields.Many2one(comodel_name="account.analytic.account", string="Account")
    company_id = fields.Many2one(comodel_name="res.company", string="Company")
    credit = fields.Float()
    debit = fields.Float()
    date = fields.Date()

    # resource can be purchase.order.line or account.invoice.line
    res_id = fields.Integer(string="Resource ID")
    res_model = fields.Char(string="Resource Model Name")

    milestone = fields.Char("Milestone")
    state = fields.Char("State")

    analytic_tag_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        relation="mis_analytic_tag_rel",
        column1="mis_analytic_id",
        column2="account_analytic_tag_id",
        string="Analytic Tags",
    )

    @api.model_cr
    def init(self):
        script = opj(os.path.dirname(__file__), "mis_analytic.sql")
        with open(script) as f:
            tools.drop_view_if_exists(self.env.cr, "mis_analytic")
            self.env.cr.execute(f.read())

            # Create many2many relation for account.analytic.tag
            tools.drop_view_if_exists(self.env.cr, "mis_analytic_tag_rel")
            self.env.cr.execute(
                """
            CREATE OR REPLACE VIEW mis_analytic_tag_rel AS
            (SELECT
                ma.id AS mis_analytic_id,
                aa_rel.tag_id AS account_analytic_tag_id
            FROM account_analytic_line_tag_rel AS aa_rel
            INNER JOIN mis_analytic AS ma ON
                ma.res_id = aa_rel.line_id
            WHERE ma.res_model = 'account.analytic.line'
            )
            """
            )
