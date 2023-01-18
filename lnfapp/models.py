from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField(default=1)
    email=models.EmailField(blank=True)
    item=models.CharField(max_length=30)
    category=models.CharField(max_length=20)
    image=models.URLField(blank=True)
    description=models.CharField(max_length=30)
    location=models.CharField(max_length=50)

