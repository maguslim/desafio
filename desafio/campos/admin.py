from django.contrib import admin
from .models import Campo, CampoFoto

class CampoFotoInline(admin.TabularInline):
    model = CampoFoto
    extra = 1

class CampoAdmin(admin.ModelAdmin):
    inlines = [CampoFotoInline]

admin.site.register(Campo, CampoAdmin)
admin.site.register(CampoFoto)
