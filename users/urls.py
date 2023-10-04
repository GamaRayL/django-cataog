from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, LoginView, verify_email, ProfileView, GenerateNewPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/<int:key>', verify_email, name='verify_email'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('generate_new_password/', GenerateNewPasswordView.as_view(), name='generate_new_password'),
    path('confirm_email/',
         TemplateView.as_view(template_name='users/confirm_email.html'),
         name='confirm_email'
         ),
]
