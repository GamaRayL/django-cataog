from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserGeneratePasswordForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label='Ваша почта:')
