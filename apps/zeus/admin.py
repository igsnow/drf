from django.contrib import admin
import xadmin

# Register your models here.
from .models import Hero

xadmin.site.register(Hero)
