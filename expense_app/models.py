from locale import currency
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserPreferences(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user) + 's' + 'preferences'


class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-date']


class Category(models.Model):
    name = models.CharField(max_length=255)


class Income(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.source

    class Meta:
        ordering = ['-date']


class Source(models.Model):
    name = models.CharField(max_length=255)