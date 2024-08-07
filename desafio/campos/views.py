from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Campo,CampoFoto
from .forms import CampoForm,CampoFotoFormSet,BuscaCampoForm
from usuarios.decorators import locador_required 


@login_required
@locador_required
def campo_list(request):
    campos = Campo.objects.filter(locador=request.user)
    return render(request, 'campos/campos_list.html', {'campos': campos})



@login_required
@locador_required
def campo_create(request):
    if request.method == 'POST':
        campo_form = CampoForm(request.POST, request.FILES)
        formset = CampoFotoFormSet(request.POST, request.FILES)

        if campo_form.is_valid() and formset.is_valid():
            campo = campo_form.save(commit=False)
            campo.locador = request.user
            campo.save()

            # Salvar imagens
            for form in formset:
                if form.cleaned_data and form.cleaned_data.get('imagem'):
                    imagem = form.cleaned_data.get('imagem')
                    if not CampoFoto.objects.filter(campo=campo, imagem=imagem).exists():
                        CampoFoto.objects.create(campo=campo, imagem=imagem)

            return redirect('campo_list')
        else:
            print("Form errors:", campo_form.errors)
            print("Formset errors:", formset.errors)
    else:
        campo_form = CampoForm()
        formset = CampoFotoFormSet(queryset=CampoFoto.objects.none())

    return render(request, 'campos/campos_form.html', {'campo_form': campo_form, 'formset': formset})

@login_required
@locador_required
def campo_update(request, pk):
    campo = get_object_or_404(Campo, pk=pk, locador=request.user)

    if request.method == 'POST':
        campo_form = CampoForm(request.POST, request.FILES, instance=campo)
        formset = CampoFotoFormSet(request.POST, request.FILES, queryset=CampoFoto.objects.filter(campo=campo))

        if campo_form.is_valid() and formset.is_valid():
            campo = campo_form.save()

            for form in formset:
                if form.cleaned_data and form.cleaned_data.get('imagem'):
                    imagem = form.cleaned_data.get('imagem')
                    if not CampoFoto.objects.filter(campo=campo, imagem=imagem).exists():
                        CampoFoto.objects.create(campo=campo, imagem=imagem)

            for form in formset.deleted_forms:
                if form.instance.pk:
                    form.instance.delete()

            return redirect('campo_list')
        else:
            print("Form errors:", campo_form.errors)
            print("Formset errors:", formset.errors)
    else:
        campo_form = CampoForm(instance=campo)
        formset = CampoFotoFormSet(queryset=CampoFoto.objects.filter(campo=campo))

    return render(request, 'campos/campos_form.html', {'campo_form': campo_form, 'formset': formset})




@login_required
@locador_required
def campo_delete(request, pk):
    campo = get_object_or_404(Campo, pk=pk, locador=request.user)
    if request.method == 'POST':
        campo.delete()
        return redirect('campo_list')
    return render(request, 'campos/campos_confirm_delete.html', {'campo': campo})


def busca_campos(request):
    query = request.GET.get('q', '') 
    tipo_gramado = request.GET.get('tipo_gramado', '')
    iluminacao = request.GET.get('iluminacao', False)
    vestiarios = request.GET.get('vestiarios', False)
    cidade = request.GET.get('cidade', '')

    campos = Campo.objects.all()

    if query:
        campos = campos.filter(
            Q(nome__icontains=query) |
            Q(endereco__icontains=query) |
            Q(descricao__icontains=query)
        )

    if tipo_gramado:
        campos = campos.filter(tipo_gramado=tipo_gramado)

    if iluminacao:
        campos = campos.filter(iluminacao=True)

    if vestiarios:
        campos = campos.filter(vestiarios=True)

    if cidade:
        campos = campos.filter(cidade__icontains=cidade)


    campos = campos.order_by('nome') 

    return render(request, 'campos/buscar_campos.html', {
        'campos': campos,
        'query': query,
        'tipo_gramado': tipo_gramado,
        'iluminacao': iluminacao,
        'vestiarios': vestiarios,
        'cidade': cidade,
        'form': BuscaCampoForm(initial={
            'q': query,
            'tipo_gramado': tipo_gramado,
            'iluminacao': iluminacao,
            'vestiarios': vestiarios,
            'cidade': cidade,
        }),
    })
