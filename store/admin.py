# store/admin.py
from django.contrib import admin
from .models import Brand, Watch

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'stock']
    prepopulated_fields = {'slug': ('title',)}