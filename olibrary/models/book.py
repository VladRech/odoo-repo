from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'olib.book'
    # _description = 'Book'
    _order = 'name'
    name = fields.Char(translate=True)
    active = fields.Boolean(default=True,)
    isbn = fields.Char()
    nauthors = fields.Integer()
    author_ids = fields.Many2many(
        comodel_name='olib.author', )
    cover = fields.Image(string='Book Cover')
