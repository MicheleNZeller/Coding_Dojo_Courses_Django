from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

class CourseTime(models.Model):
    names = models.CharField(max_length = 45)
    description = models.CharField(max_length = 100)
    # year = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Create your models here.
