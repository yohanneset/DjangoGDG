from django.db import models
# Create your models here.

class Loan(models.Model):
    name = models.CharField(max_length=250)
    amount = models.PositiveIntegerField()
    date = models.DateField()
    reason = models.TextField()