from django.contrib import admin
from .models import Campo, CampoFoto, Reserva

class CampoFotoInline(admin.TabularInline):
    model = CampoFoto
    extra = 1

class CampoAdmin(admin.ModelAdmin):
    inlines = [CampoFotoInline]

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('campo', 'usuario', 'data_reserva', 'hora_inicio', 'hora_fim', 'valor_total', 'criado_em')
    list_filter = ('campo', 'usuario', 'data_reserva')
    search_fields = ('campo__nome', 'usuario__username', 'data_reserva')

admin.site.register(Campo, CampoAdmin)
admin.site.register(CampoFoto)
admin.site.register(Reserva, ReservaAdmin)
