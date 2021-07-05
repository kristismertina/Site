from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Task (models.Model):
    title = models.CharField('Название',max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

