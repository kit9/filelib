# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing tailsde.
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class Project(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    account_analytic_task_id = fields.Many2one('account.analytic.tag', '分析帐号包')

    @api.multi
    def action_show_structure(self):
        ids = []
        ids += self.ids
        id_need_reduce = []
        for item in self:
            if item.project_child_complete_ids:
                ids += item.project_child_complete_ids.ids
                id_need_reduce += item.project_child_complete_ids
                while id_need_reduce:
                    if id_need_reduce[0].project_child_complete_ids:
                        id_need_reduce += id_need_reduce[0].project_child_complete_ids
                        ids += id_need_reduce[0].project_child_complete_ids.ids
                        id_need_reduce.pop(0)
                    else:
                        id_need_reduce.pop(0)

        return {
            "name": _("WBS Structure View"),
            "type": 'ir.actions.act_window',
            "res_model": 'project.project',
            # "views": [[self.env.ref('e2yun_cge_project_wbs_extends.project_project_tree_view').id, "tree"]],
            "views": [[self.env.ref('e2yun_cge_project_wbs_extends.project_project_tree_view').id, "tree"]],
            # "target": 'new',
            "domain": [['id', '=', ids]],
            "context": {"create": False},
        }

    # return {
    #     "type": "ir.actions.act_window",
    #     "res_model": "sale.order",
    #     "views": [[self.env.ref('sale_subscription.sale_order_view_tree_subscription').id, "tree"],
    #               [self.env.ref('sale.view_order_form').id, "form"],
    #               [False, "kanban"], [False, "calendar"], [False, "pivot"], [False, "graph"]],
    #     "domain": [["id", "in", sales.ids]],
    #     "context": {"create": False},
    #     "name": _("Sales Orders"),
    # }
