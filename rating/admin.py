from django.contrib import admin

from rating.models import RatingStar, Rating

admin.site.register(Rating)
admin.site.register(RatingStar)
