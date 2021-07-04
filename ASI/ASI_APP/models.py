# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Insurance(models.Model):
  #id = models.AutoField()
  ins_id = models.IntegerField(unique=True)
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=100)
  startdate = models.DateField(r'%d/%m/%Y')
  mat_date = models.DateField(r'%d/%m/%Y')
  amount = models.FloatField()
