from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import DOITLIST
from .forms import DOITLISTDetailForm, DOITLISTCreateForm

# Create your views here.
def index(request):
    todo_list = DOITLIST.objects.filter(is_done__exact=False).order_by('done_date')
    done_list = DOITLIST.objects.filter(is_done__exact=True).order_by('done_date')
    
    context = {
        'todo_list': todo_list,
        'done_list': done_list,
    }
    
    return render(request, 'doit/doitlist.html', context)

def detail(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    if request.method == "POST":
        form = DOITLISTDetailForm(request.POST, instance=doit_item)
        if form.is_valid():
            doit_item = form.save(commit=False)
            doit_item.save()
            return redirect('doit:index')
    else:
        form = DOITLISTDetailForm(instance=doit_item)
        
    context = {
        'form': form
    }
    return render(request, 'doit/detail_form.html', context=context)

def create_item(request):
    if request.method == "POST":
        form = DOITLISTCreateForm(request.POST)
        if form.is_valid():
            doit_item = form.save(commit=False)
            doit_item.create_date = timezone.now()
            doit_item.is_done = False
            doit_item.save()
            return redirect('doit:index')
    else:
        form = DOITLISTCreateForm()
    context = {
        'form': form
    }
    return render(request, 'doit/create_form.html', context=context)

def finish_item(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    doit_item.is_done = True
    doit_item.save()
    return redirect('doit:index')

def delete_item(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    doit_item.delete()
    return redirect('doit:index')
    
def back_item(request, doit_item_id):
    doit_item = get_object_or_404(DOITLIST, pk=doit_item_id)
    doit_item.is_done = False
    doit_item.save()
    return redirect('doit:index')