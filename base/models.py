from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ratings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matches_played = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    

    @property
    def contribution_ratio(self):
        return (self.goals + self.assists)/self.matches_played


    @property
    def points(self):
        return (5*self.goals) + (2*self.assists)

    class Meta:
        order_with_respect_to = 'goals'
