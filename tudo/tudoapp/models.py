from django.db import models
class tudoapp(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    mob=models.IntegerField()
    password=models.CharField(max_length=30)

# Create your models here.
