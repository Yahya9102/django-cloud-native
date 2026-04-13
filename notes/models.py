from django.db import models

from categories.models import Category


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="notes",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title