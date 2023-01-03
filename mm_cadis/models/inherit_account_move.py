
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from lxml import etree, objectify
from lxml.objectify import fromstring
from odoo import api, fields, models, _, tools, release

class InheritAccount(models.Model):
    _inherit = 'account.move'
    _description = 'inherit account'

    mm_taxex = fields.Many2many('res.partner', string='mm_taxe')
    