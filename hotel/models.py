# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotel(models.Model):
      #id
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=4)
    img = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    description = models.TextField()