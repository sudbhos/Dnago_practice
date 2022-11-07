from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=10)
    surname=models.CharField(max_length=10)
    salary=models.FloatField()
    location=models.CharField(max_length=100)
    empid=models.IntegerField()
    def __str__(self):
        return self.name