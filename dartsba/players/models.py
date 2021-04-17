from django.db import models


class Players(models.Model):

    username = models.CharField(max_length=99, null=False, blank=False)
    email = models.CharField(max_length=99, null=False, blank=False)
    first_name = models.CharField(max_length=99, null=False, blank=False)
    last_name = models.CharField(max_length=99, null=False, blank=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = "players"
        verbose_name = "player"
        ordering = ('-created_at',)
