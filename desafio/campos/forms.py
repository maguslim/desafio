from django import forms
from .models import Campo, CampoFoto
from django.forms import modelformset_factory


class CampoForm(forms.ModelForm):
    class Meta:
        model = Campo
        fields = ['nome', 'endereco', 'descricao', 'preco_hora', 'tipo_gramado', 'iluminacao', 'vestiarios', 'cidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco_hora'].widget = forms.TextInput(attrs={
            'placeholder': 'O preço por hora deve ser no mínimo R$ 1,00.',
            'id': 'id_preco_hora'
        })

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if Campo.objects.exclude(pk=self.instance.pk).filter(nome=nome).exists():
            raise forms.ValidationError("Já existe um campo com este nome.")
        return nome

class CampoFotoForm(forms.ModelForm):
    class Meta:
        model = CampoFoto
        fields = ['imagem']

CampoFotoFormSet = modelformset_factory(CampoFoto, form=CampoFotoForm)



class BuscaCampoForm(forms.Form):
    q = forms.CharField(required=False, label='Buscar')
    tipo_gramado = forms.ChoiceField(choices=[('', 'Todos'), ('natural', 'Natural'), ('sintetico', 'Sintético')], required=False)
    iluminacao = forms.BooleanField(required=False, label='Com Iluminação')
    vestiarios = forms.BooleanField(required=False, label='Com Vestiários')
    cidade = forms.CharField(required=False, label='Cidade') 