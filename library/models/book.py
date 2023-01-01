import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'lib.book'
    _description = 'Book'
    name = fields.Char()
    active = fields.Boolean(default=True,)
    isbn = fields.Char()
    author_ids = fields.Many2many(
        comodel_name='lib.author', )
