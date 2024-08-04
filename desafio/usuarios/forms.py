from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nome de Usuário',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }
        error_messages = {
            'username': {
                'required': 'Este campo é obrigatório.',
                'max_length': 'Máximo de 150 caracteres.',
                'invalid': 'Caracteres inválidos. Use apenas letras, números e @/./+/-/_',
            },
            'email': {
                'required': 'Este campo é obrigatório.',
                'invalid': 'Informe um endereço de email válido.',
            },
            'password1': {
                'required': 'Este campo é obrigatório.',
            },
            'password2': {
                'required': 'Este campo é obrigatório.',
                'password_mismatch': 'As senhas não coincidem.',  # Ajuste a mensagem de erro aqui
            },
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class VerificationForm(forms.Form):
    code = forms.CharField(max_length=6)


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email")

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Endereço de Email não encontrado.")
        return email


class PasswordResetVerifyForm(forms.Form):
    code = forms.CharField(max_length=6)


class PasswordResetCompleteForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        if user is None:
            raise ValueError("User is required")
        # Passa o user para o SetPasswordForm
        super().__init__(user=user, *args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("As senhas não coincidem.")

        if self.user and new_password1:
            if self.user.check_password(new_password1):
                raise forms.ValidationError(
                    "A nova senha não pode ser igual à senha antiga.")

        return cleaned_data

    def save(self, commit=True):
        # Chama o save do SetPasswordForm para atualizar a senha
        return super().save(commit=commit)


class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'profile_picture']


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
