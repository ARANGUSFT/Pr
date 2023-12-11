from django.shortcuts import render, redirect
from .forms import UsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reconocimiento')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/registro_usuario.html', {'form': form})
