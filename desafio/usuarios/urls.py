from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    RegisterView, VerifyCodeView, LoginView, HomeView, LogoutView,
    PasswordResetRequestView, PasswordResetVerifyView, PasswordResetCompleteView, profile_view,
)

urlpatterns = [
    path('registrar-se/', RegisterView.as_view(), name='register'),
    path('verificacao/', VerifyCodeView.as_view(), name='verificacao'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('trocar-senha/', PasswordResetRequestView.as_view(), name='trocar-senha'),
    path('password-reset-verify/', PasswordResetVerifyView.as_view(), name='password_reset_verify'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', profile_view, name='profile'),
    path('', HomeView.as_view(), name='home'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


