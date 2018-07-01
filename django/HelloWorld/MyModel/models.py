# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
#   ClassName : the table name in database.
#   FieldName : column name in table.
class Test(models.Model):
    name = models.CharField(max_length=20)
