from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')



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
    objects = models.Manager()  # Default manager
    published = PublishedManager()

    class Meta:
        ordering = ['-published_at']

    def get_absolute_url(self):
        return reverse('post_details', args=[self.id])

    def __str__(self):
        return self.title