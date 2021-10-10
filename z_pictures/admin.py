from django.contrib import admin


# Register your models here.
from z_pictures.models import Category, Image, Location

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)
