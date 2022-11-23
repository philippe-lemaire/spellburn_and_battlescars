from django.db import models


class Creature(models.Model):
    name = models.CharField(max_length=200)
    hp = models.IntegerField()
    body = models.IntegerField()
    mind = models.IntegerField()
    armor = models.IntegerField(null=True, blank=True)
    attack = models.CharField(blank=True, max_length=60)
    special = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}."
