from django.db import models

# Create your models here.
class Client(models.Model):
    username = models.CharField(unique=True, max_length=50, null=False)
    password = models.CharField(max_length=80, null=False)
    name = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    age = models.IntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    imc = models.FloatField(null=True)
    geb = models.FloatField(null=True)
    eta = models.FloatField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.username}'


