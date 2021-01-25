from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=54)
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField()
    password = models.CharField(max_length=127)
    re_password = models.CharField(max_length=127)


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class Nk(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class Jo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
