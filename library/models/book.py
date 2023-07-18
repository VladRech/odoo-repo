import logging
from odoo import api, models, fields
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'lib.book'
    _description = 'Book'
    _order = 'name'
    name = fields.Char('Book name', required=True)
    active = fields.Boolean(default=True,)
    isbn = fields.Char('ISBN')
    year = fields.Integer('Year of publication')
    pages = fields.Integer('Number of pages')
    author_ids = fields.Many2many(
        comodel_name='lib.author', )
    age = fields.Integer('Years since release',
        compute='compute_age',)

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
            '*** Помилка: назва книги повинна бути унікальною! ***')
        # ('positive_pages', 'CHECK(pages>0)',
        #     '*** Помилка: кількість сторінок книги повнна бути додатньою! ***')
        # ('modern_book', 'CHECK(year>=1900)',
        #  '*** Помилка: книги в бібліотеці не можуть бути старовинними! ***')
    ]

    @api.constrains('year')
    def _check_year(self):
        # import pdb; pdb.set_trace()
        for record in self:
            if record.year < 1900:
                raise models.ValidationError(
                    '*** Помилка: книги в бібліотеці не можуть бути старовинними!')
            elif record.year > fields.Date.today().year:
                raise models.ValidationError(
                    '*** Помилка: рік видання книги не може бути більшим від поточного року!')

    @api.constrains('pages')
    def _check_pages(self):
        for record in self:
            if record.pages <= 0:
                raise models.ValidationError(
                    '*** Помилка: кількість сторінок книги повнна бути додатньою!')

    @api.depends('year')
    def compute_age(self):
        today = fields.Date.today()
        cur_year = today.year
        for book in self:
            if book.year:
                age = cur_year - book.year
                book.age = age
            else:
                book.age = 0
