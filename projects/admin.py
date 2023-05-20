from django.contrib import admin
from .models import Project
from .models import Classes
from .models import Sword_img
from .models import Hotel
from .models import Blog
from django.utils.html import format_html

# Register your models here.
# for admin page

# samm as in modles.py for name and what not


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']
    list_filter = ['title']


@admin.register(Classes)  # can also add a date time filter
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['class_title']
    search_fields = ['class_title']
    list_filter = ['class_title']


@admin.register(Sword_img)
class Sword_imgAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.image.url ))
    list_display = ['title', 'thumbnail']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']
