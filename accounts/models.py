from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import os
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )
    first_name = models.CharField(
        max_length = 50,
        null = True,
        blank= True,
    )
    last_name = models.CharField(
        max_length = 50,
        null = True,
        blank= True,
    )
    bio = models.CharField(
        max_length = 250,
        null = True,
        blank = True,
    )
    headline = models.CharField(
        max_length = 200,
        null = True,
        blank = True,
    )
    gender = models.CharField(
        max_length= 50,
        null = True,
        blank = True,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Prefer not to say', 'Prefer not to say'),
        ],
    )
    image = models.ImageField(
        upload_to = 'profile_pics',
        default = 'profile_pics/default-user.png',
    )
    slug = models.SlugField(
        null= True,
        blank=True,
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_image_url(self):
        if self.image and hasattr(self.image, 'name') and self.image.name != '':
            image_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            if os.path.exists(image_path):
                return self.image.url
            else:
                return os.path.join(settings.MEDIA_URL, 'profile_pics/default-user.png')
        return os.path.join(settings.MEDIA_URL, 'profile_pics/default-user.png')

    def __str__(self):
        return f'{self.user.username} profile'
