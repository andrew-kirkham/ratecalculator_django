# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RateRequest(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
