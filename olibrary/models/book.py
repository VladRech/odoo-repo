from odoo import api, models, fields
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
    publisher_id = fields.Many2one(
        'res.partner', string='Publisher',
        ondelete='set null',)
    publisher_city = fields.Char(
        'Publisher city',
        related='publisher_id.city',
        readonly=True,)
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
        'State', default="draft")

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
             ('available', 'borrowed'),
             ('borrowed', 'available'),
             ('available', 'lost'),
             ('borrowed', 'lost'),
             ('lost', 'available')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                continue

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')
