# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InheritAccount(models.Model):
    _inherit = 'account.move'
  

   #mm_taxe_inh = fields.One2many('res.partner', 'mm_taxe', string='TAX ID')
    
    mm_taxe_inh = fields.Char('TAX id', related='res_partner.mm_taxe', readonly=True)