from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

GAME_STATUS_CHOICES = (
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('FW', 'First Player Wins'),
    ('SW', 'Second Player Wins'),
    ('D', 'Draw')
)


@python_2_unicode_compatible
class Game(models.Model):
    firstPlayer = models.ForeignKey(User, related_name="gameFirstPlayer")
    secondPlayer = models.ForeignKey(User, related_name="gameSecondPlayer")
    startTime = models.DateTimeField(auto_now_add=True)
    lastActive = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, default='F', choices=GAME_STATUS_CHOICES)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    byFirstPlayer = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)


