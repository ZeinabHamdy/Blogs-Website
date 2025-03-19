
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,

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
        upload_to = 'assets/profile_pics',
        default = 'assets/profile_pics/default-user.png',
    )

    def __str__(self):
        return f'{self.user.username} profile'