# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    mm_taxe = fields.Many2one('res.partner', string='TAX ID')
