from django.contrib import admin
from django import forms
from .models import Ratings

class RatingAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude admins from the user selection dropdown
        self.fields['user'].queryset = self.fields['user'].queryset.exclude(is_superuser=True)

class RatingAdmin(admin.ModelAdmin):
    form = RatingAdminForm
    list_display = ['player','goals','assists','matches_played']
    list_filter = ['goals']

    def player(self,obj):
        return obj.user.username
    player.short_description = 'player'

admin.site.register(Ratings, RatingAdmin)


# @admin.register(Ratings)
# class RatePlayers(admin.ModelAdmin):
#     list_display = ['user','goals','assists']


    
