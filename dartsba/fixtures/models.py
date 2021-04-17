from django.contrib.auth.models import User
from django.db import models

from dartsba.matches.models import Matches


class Fixtures(models.Model):

    GAME_RESULT = [
        (0, 'Lose'),
        (1, 'Draw'),
        (2, 'WO'),
        (3, 'Victory')
    ]

    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ton = models.IntegerField(default=0)
    ton40 = models.IntegerField(default=0)
    ton70 = models.IntegerField(default=0)
    ton80 = models.IntegerField(default=0)
    result = models.IntegerField(choices=GAME_RESULT, default=0)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = "fixtures"
        verbose_name = "fixture"
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.winner)
