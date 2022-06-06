from django.contrib import admin
from master.models import Category, Master, Favorite

admin.site.register(Master)
admin.site.register(Category)
admin.site.register(Favorite)