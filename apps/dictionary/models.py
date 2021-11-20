from django.db import models
from django.contrib.auth.models import User
from grammar.config import *

MAIN_CLASSES = ((v, v) for v in MAIN_CLASSES)

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    abv = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=100)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    main_class = models.CharField(choices=MAIN_CLASSES, default='noun', max_length=100)
    sub_class = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-word']

    def __str__(self):
        return self.word


# class Translations(models.Model)