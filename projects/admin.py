from django.contrib import admin
from .models import Project
from .models import Classes

# Register your models here.
# for admin page

#samm as in modles.py for name and what not

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    pass
