from django.contrib import admin

# Register your models here.
from .models import Categories,News

admin.site.register(Categories)
admin.site.register(News)
