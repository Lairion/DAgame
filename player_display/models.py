# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Character(models.Model):
    class Meta:
        pass

    DICE = ((4,"Four"),(6,"Six"),(8,"Eight"),(10,"Ten"),(12,"Twelf"))
    user = models.ForeignKey(User)
    name_character = models.CharField(max_length=100)
    team = models.ManyToManyField('self')
    character_concept = models.TextField()
    look = models.TextField()
    nayword = models.TextField(null=True,blank=True)
    dexterity = models.IntegerField(choices=DICE,default=4)
    smart = models.IntegerField(choices=DICE,default=4)
    nature = models.IntegerField(choices=DICE,default=4)
    power = models.IntegerField(choices=DICE,default=4)
    stamina = models.IntegerField(choices=DICE,default=4)
    step = models.IntegerField(default=6)
    run = models.IntegerField()
    defence = models.IntegerField(default=2)
    tenacity = models.IntegerField(default=2)
    charisma = models.IntegerField(default=-2)
    

