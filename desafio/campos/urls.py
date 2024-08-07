from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.busca_campos, name='busca_campos'),
    path('SeusCampos/', views.campo_list, name='campo_list'),
    path('NovoCampo/', views.campo_create, name='campo_create'),
    path('<int:pk>/editar/', views.campo_update, name='campo_update'),
    path('<int:pk>/deletar/', views.campo_delete, name='campo_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
