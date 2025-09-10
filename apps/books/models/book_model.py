from django.db import models

class Book(models.Model):
    """Model representing a book with various attributes and relationships."""
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255, null=False)
    summary = models.TextField(null=False)
    language = models.CharField(max_length=2, null=False)
    publication_date = models.DateField(null=False)
    cover_url = models.TextField(null=True)
    pages = models.IntegerField(null=False)
    collection = models.ForeignKey(
        'Collection',
        on_delete=models.PROTECT,
        null=False,
        related_name='books'
    )

    authors = models.ManyToManyField(
        'Author',
        related_name='books'
    )
    genres = models.ManyToManyField(
        'Genre',
        related_name='books'
    )
    publishers = models.ManyToManyField(
        'Publisher',
        related_name='books'
    )
    themes = models.ManyToManyField(
        'Theme',
        related_name='books'
    )

