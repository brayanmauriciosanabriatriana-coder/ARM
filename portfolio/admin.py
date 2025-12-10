from django.contrib import admin
from .models import Proyecto

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # ← se muestran como solo lectura

admin.site.register(Proyecto, ProjectAdmin)
