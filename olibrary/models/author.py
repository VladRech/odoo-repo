import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'lib.author'
    _description = 'Author'
    _order = 'name'
    name = fields.Char()
    active = fields.Boolean(default=True, )
    book_ids = fields.Many2many(
        comodel_name='lib.book',
        ondelete='cascade',)
