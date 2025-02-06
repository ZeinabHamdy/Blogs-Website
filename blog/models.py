from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(
        max_length=100,
        unique=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=15,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
        ],
        default='draft',
    )


    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title