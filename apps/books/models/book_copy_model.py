from django.db import models

class BookCopy(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
        ('lost', 'Lost'),
    ]

    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        db_column='book_isbn',
        related_name='copies',
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
