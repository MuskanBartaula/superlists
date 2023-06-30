from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item

def home(request):
    # if request.method == 'POST':
    #     new_text = request.POST.get('item_text', '')
    #     Item.objects.create(text=new_text)
    #     return redirect('/lists/the-only-list-in-the-world')
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home.html', context)

def new_list(request):
    Item.objects.create(text=request.POST.get('item_text'))
    return redirect('/lists/the-only-list-in-the-world')

    

def view_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'list.html', context)