from django.contrib import admin
from .models import UserProfile  # Importa o modelo

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'profile_picture')  # Campos a serem exibidos na lista
    search_fields = ('user__username', 'phone_number')  # Campos pesquisáveis
    list_filter = ('user',)  # Filtros laterais

# Registra o modelo e a classe de administração no site admin
admin.site.register(UserProfile, UserProfileAdmin)
