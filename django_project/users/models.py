from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class UserDummy(models.Model):
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.author


class Ratings(models.Model):
    contest=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    def __str__(self):
        return self.contest