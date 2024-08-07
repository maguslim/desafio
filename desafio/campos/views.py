from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Campo
from .forms import CampoForm
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
        form = CampoForm(request.POST, request.FILES)
        
        if form.is_valid():
            campo = form.save(commit=False)
            campo.locador = request.user
            campo.save()
            return redirect('campo_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = CampoForm()
    return render(request, 'campos/campos_form.html', {'form': form})

@login_required
@locador_required
def campo_update(request, pk):
    campo = get_object_or_404(Campo, pk=pk, locador=request.user)
    if request.method == 'POST':
        form = CampoForm(request.POST, request.FILES, instance=campo)
        
        if form.is_valid():
            form.save()
            return redirect('campo_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = CampoForm(instance=campo)
    return render(request, 'campos/campos_form.html', {'form': form})

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
    campos = Campo.objects.all()

    if query:
        campos = campos.filter(
            Q(nome__icontains=query) |
            Q(endereco__icontains=query) |
            Q(descricao__icontains=query)
        )

    return render(request, 'campos/buscar_campos.html', {'campos': campos, 'query': query})
