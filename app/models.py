from django.db import models

# Create your models here.
class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    image=models.ImageField(upload_to="images/")
    