from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    pfp = models.ImageField(
        null=True, upload_to="uploads/pfp/", default="../static/noimage.png"
    )

    def __str__(self):
        return self.user.username
