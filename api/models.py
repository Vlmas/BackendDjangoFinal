from django.db import models
from django.utils.timezone import now


class BookJournalBase(models.Model):
    name = models.CharField(default='', max_length=128)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    created_at = models.DateTimeField(default=now(), blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Book Journal Base'


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=1)
    genre = models.CharField(default='', max_length=64)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.id}: {self.genre}'


class Journal(BookJournalBase):
    type = models.CharField(default='Travel', max_length=64)
    publisher = models.CharField(default='Almas', max_length=64)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def __str__(self):
        return f'{self.id}: {self.type}'
