from operator import index
from turtle import done
from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import kitnet
from django.contrib.auth.decorators import login_required
from .forms import kitnetForms
from django.contrib import messages


@login_required
def manage(request):
           
    filter = request.GET.get('filter')
    if filter:
        interfaces = kitnet.objects.filter(Tam_Kitnet=filter, user=request.user)
        return render(request, 'interfaces/index.html', {"interfaces": interfaces})
    else:
         interfaces = kitnet.objects.all().order_by('-created_at').filter(user=request.user)
         return render(request, 'interfaces/index.html', {"interfaces": interfaces})


@login_required
def newKitnet(request):
    if request.method == 'POST':
        form = kitnetForms(request.POST)
        if form.is_valid():
            kitnet = form.save(commit=False)
            kitnet.done = 'Alugado'
            kitnet.user = request.user
            kitnet.save()
            return redirect('/')
        else:
            messages.info(request, 'JÁ EXISTE UM KITNET COM ESSES DADOS')
            return render(request, 'interfaces/newKitnet.html', {"form": form})
    else:
        form = kitnetForms()
        return render(request, 'interfaces/newKitnet.html', {"form": form})

@login_required
def editKitnet(request, id):
    edit = get_object_or_404(kitnet, pk=id)
    form = kitnetForms(instance=edit)

    if(request.method == 'POST'): 
        form = kitnetForms(request.POST, instance=edit)
        if(form.is_valid()):
            edit.save()
            return redirect('/')
        else:
            messages.info(request, 'JÁ EXISTE UM KITNET COM ESSES DADOS')
            return render(request, 'interfaces/editKitnet.html', {'form' : form, 'edit' : edit})
    else:
        return render(request, 'interfaces/editKitnet.html', {'form' : form, 'kitnet' : kitnet})

@login_required
def deleteKitnet(request, id):
    deletKit = get_object_or_404(kitnet, pk=id)
    deletKit.delete()
    messages.info(request, 'Kitnet deletado com sucesso!!')
    return redirect('/')