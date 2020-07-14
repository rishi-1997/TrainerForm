from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    trainer_id = models.IntegerField()
    address = models.CharField(max_length=50)
