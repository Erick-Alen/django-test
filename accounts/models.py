from django.db import models


# class name in PascalCase
class Account(models.Model):
    # string => Charfield
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    # YYYY - MM - DD
    birthDate = models.DateField(null=True)
    isMarried = models.BooleanField(default=False)
