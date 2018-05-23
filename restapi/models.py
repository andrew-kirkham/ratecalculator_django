# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Rate(models.Model):
    days = models.CharField(max_length=100, blank=True, default='')
    times = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()

    class Meta:
        ordering = ('price',)


class RateRequest(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
