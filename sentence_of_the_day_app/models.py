from django.db import models

# Create your models here
class sentences(models.Model):
    bucket_id = models.IntegerField(max_length = 30, primary_key = True)
    sentence = models.CharField(max_length = 100)

