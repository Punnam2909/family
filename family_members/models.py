from django.db import models

# Create your models here.

class Punnam(models.Model):
    Name=models.CharField(max_length=90)
    Description=models.TextField()
    Qualification=models.CharField(max_length=20)
    kids=models.IntegerField(default=True)

def __str__(self):
    return self.name

class Meta:
    verbose_name="Punnam"
    verbose_name_plural = "Punnams"


