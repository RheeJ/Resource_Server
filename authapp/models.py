# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class QuarkX_User(models.Model):
    isSuper = models.BooleanField(default=False)
    isReport = models.BooleanField(default=False)
    isNormal = models.BooleanField(default=True)
    email = models.CharField(max_length=100)
