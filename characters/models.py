from django.db import models
from django.conf import settings


# Create your models here.


class Character(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.TextField(max_length=200)
    archetype = models.TextField(max_length=200)
    origin = models.TextField(max_length=400, null=True, blank=True)
    background = models.TextField(max_length=200, null=True, blank=True)
    armor = models.SmallIntegerField(default=0, blank=True, null=True)
    hp = models.SmallIntegerField(default=0, blank=True, null=True)
    current_hp = models.SmallIntegerField(default=0, blank=True, null=True)
    body = models.SmallIntegerField(default=0, blank=True, null=True)
    mind = models.SmallIntegerField(default=0, blank=True, null=True)
    luck = models.SmallIntegerField(default=0, blank=True, null=True)
    gear = models.TextField()
    gold = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
