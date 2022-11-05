from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormLInks
from .models import Links
from django.shortcuts import redirect

def home(request):
    form = FormLInks()
    status = request.GET.get('status') 
    return render(request, 'home.html', {'form': form, 'status': status})

def val_link(request):
    form = FormLInks(request.POST)
    link_encurtado = form.data['link_encurtado']
    links = Links.objects.filter(link_encurtado = link_encurtado)
    if len(links) > 0:
        return redirect ("/?status=1")

    if form.is_valid():
        try:
            form.save()
            return HttpResponse (f"Seu link foi criado com sucesso e é: http://127.0.0.1:8000/{form.data['link_encurtado']}")
        except:
            return HttpResponse ("erro interno do sistema")

def redirecionar (request, link):
    links = Links.objects.get(link_encurtado = link)
    if len(links) ==0:
        return redirect ('/')
    print(links)
    return redirect(links[0].link_redirecionado)


    