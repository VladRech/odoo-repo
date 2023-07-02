from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'olib.author'
    # _description = 'Author'
    _order = 'name'
    name = fields.Char(translate=True)
    active = fields.Boolean(default=True, )
    book_ids = fields.Many2many(
        comodel_name='olib.book',
        ondelete='cascade',)
