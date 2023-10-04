import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LoginView as BaseLogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView

from users.forms import UserRegisterForm, UserGeneratePasswordForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        key = str(random.randint(1, 99999))
        form.instance.key = key
        user = form.save()

        verify_email_url = reverse('users:verify_email', args=[key])

        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Вы зарегистрировались на нашей платформе. '
                    f'Для продолжения регистрации перейдите по ссылке {get_current_site(self.request)}{verify_email_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_valid(form)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mainapp:products')


class Logout(BaseLogoutView):
    pass


class ProfileView(UpdateView):
    pass


def verify_email(request, key):
    user = User.objects.get(key=key)

    if not user.is_active:
        user.is_active = True
        user.save()
        return HttpResponse("Email успешно подтвержден!")
    else:
        return HttpResponse("Email уже подтвержден!")


class GenerateNewPasswordView(FormView):
    model = User
    form_class = UserGeneratePasswordForm
    template_name = 'users/generate_new_password.html'
    success_url = HttpResponse('Пароль сброшен')

    def form_valid(self, form):
        user = form.save()
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_mail(
            subject='Вы сменили пароль',
            message=f'Ваш новый пароль {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
