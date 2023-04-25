from django.contrib import admin
from .models import About,Videos

# Register your models here.

@admin.register(About)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('detail',)
    

@admin.register(Videos)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name','about_project','video_link','date')