from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='Default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self,*args, **kwargs):
        # this override the super().save() so taht we can add in more functionalities
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>600 or img.width>600:
            output_size=(600,600)
            img.thumbnail(output_size)
            img.save(self.image.path)