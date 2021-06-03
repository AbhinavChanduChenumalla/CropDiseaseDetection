from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Uploads(models.Model):
    img = models.ImageField(upload_to='media/',blank=True,null=True)
    user = models.ForeignKey(User, default=1,null=True, on_delete=models.SET_NULL)
    path = models.TextField(null=True)