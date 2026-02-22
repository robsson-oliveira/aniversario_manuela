from django.shortcuts import render, redirect
from .forms import ConfirmacaoForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def confirmar_presenca(request):
    if request.method == 'POST':
        form = ConfirmacaoForm(request.POST)
        if form.is_valid():
            confirmacao = form.save()

            send_mail(
                'Confirmação de Presença – Aniversário da Manuela 🎉',
                'Obrigada por confirmar!\n\n📍 Local: Rua X, nº Y\n🕒 Horário: 15h',
                'seuemail@gmail.com',
                [confirmacao.email],
                fail_silently=False,
            )

            return redirect('obrigado')
    else:
        form = ConfirmacaoForm()

    return render(request, 'confirmar.html', {'form': form})

def obrigado(request):
    return render(request, 'obrigado.html')