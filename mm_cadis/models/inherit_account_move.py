# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritAccount(models.Model):
    _inherit = 'account.move'
  

    mm_taxe = fields.Many2many('res.partner', string='mm_taxe')
    