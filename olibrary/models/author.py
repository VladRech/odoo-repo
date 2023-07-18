from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'olib.author'
    # _description = 'Author'
    _order = 'name'
    active = fields.Boolean(default=True, )
    first_name = fields.Char('First name', translate=True)
    last_name = fields.Char('Last name', translate=True)
    full_name = fields.Char('Full name', translate=True)
    name = fields.Char('Short name', translate=True)
    book_ids = fields.Many2many(
        comodel_name='olib.book',
        ondelete='cascade',)

    @api.onchange('first_name', 'last_name')
    def set_name(self):
        if self.first_name and self.last_name:
            self.full_name = f'{self.first_name} {self.last_name}'
            initial = self.first_name[0]
            self.name = f'{self.last_name}, {initial}.'
