from django import forms
from .models import Campo
from django.forms.models import inlineformset_factory

class CampoForm(forms.ModelForm):
    class Meta:
        model = Campo
        fields = ['nome', 'endereco', 'descricao', 'preco_hora']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco_hora'].widget = forms.TextInput(attrs={
            'placeholder': 'O preço por hora deve ser no mínimo R$ 1,00.',
            'id': 'id_preco_hora'
        })
