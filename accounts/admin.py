from django.contrib import admin
from .models import User

# Register your models here.


admin.site.register(User)


admin.site.index_title = "Atanfo Ny3 Nyame"
admin.site.site_header = "Atanfo Ny3 Nyame"
admin.site.site_title = "Ratings Dashboard"