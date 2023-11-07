from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import DOITLIST
from .forms import DOITLISTForm

# Create your views here.
def index(request):
    todo_list = DOITLIST.objects.filter(is_done__exact=False)
    done_list = DOITLIST.objects.filter(is_done__exact=True)
    
    context = {
        'todo_list': todo_list,
        'done_list': done_list,
    }
    
    return render(request, 'doit/doitlist.html', context)

def detail(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    if request.method == "POST":
        form = DOITLISTForm(request.POST, instance=doit_item)
        if form.is_valid():
            doit_item = form.save(commit=False)
            doit_item.save()
            return redirect('doit:index')
    else:
        form = DOITLISTForm(instance=doit_item)
        
    context = {
        'form': form
    }
    return render(request, 'doit/detail_form.html', context=context)

def create_item(request):
    if request.method == "POST":
        form = DOITLISTForm(request.POST)
        if form.is_valid():
            doit_item = form.save(commit=False)
            doit_item.create_date = timezone.now()
            doit_item.save()
            return redirect('doit:index')
    else:
        form = DOITLISTForm()
    context = {
        'form': form
    }
    return render(request, 'doit/detail_form.html', context=context)

def finish_item(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    doit_item.is_done = True
    doit_item.save()
    return redirect('doit:index')

def delete_item(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    doit_item.delete()
    return redirect('doit:index')
    