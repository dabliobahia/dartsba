from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Stat(models.Model):
    """Stat Class on OneToOne with User models"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matches = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    maxout = models.IntegerField(default=0)
    best21 = models.IntegerField(default=0)
    tons = models.IntegerField(default=0)
    ton40 = models.IntegerField(default=0)
    ton70 = models.IntegerField(default=0)
    ton80 = models.IntegerField(default=0)
    bull = models.IntegerField(default=0)
    doublebull = models.IntegerField(default=0)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name_plural = "stats"
        verbose_name = "stat"
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.win)

@receiver(post_save, sender=User)
def create_user_stat(sender, instance, created, **kwargs):
    if created:
        Stat.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_stat(sender, instance, **kwargs):
    instance.stat.save()