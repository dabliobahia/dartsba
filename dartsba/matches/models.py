from django.db import models


class Matches(models.Model):
    GAME_TYPE = [
        (1, '101'),
        (2, '201'),
        (3, '301'),
        (4, '401'),
        (5, '501'),
        (6, 'RUMO AO TOPO')
    ]
    game = models.IntegerField(choices=GAME_TYPE, default=1)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = "macthes"
        verbose_name = "macth"
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.game+' '+self.created_at)
