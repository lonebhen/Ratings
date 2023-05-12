from django.db import models
from accounts.models import User




class Ratings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = "Ratings"
        order_with_respect_to = "goals"



    def __str__(self):
        return f"{self.user}"
