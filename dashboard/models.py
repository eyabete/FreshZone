from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='seller_photos', blank=True, null=True)
    
    def __str__(self):
        return self.user.full_name
    
class UserImage(models.Model):
    user = models.ForeignKey(UserProfile, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='seller_photos')

    def __str__(self):
        return f"Image for {self.user.full_name}"
