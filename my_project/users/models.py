from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

# model for uploading picture for profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # method to resize images
    def save(self, **kwargs):
        super().save()

        image = Image.open(self.image.path)

        if image.height > 200 or image.width > 200:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.image.path)
