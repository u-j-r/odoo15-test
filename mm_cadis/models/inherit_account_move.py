# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    mm_taxe_rel = fields.Many2one('res.partner', 'mm_taxe', string='TAX ID',
    ondelete='set null',
    context={},
    domain=[],
    )
