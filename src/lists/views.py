from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item

def home(request):
    if request.method == 'POST':
        new_text = request.POST.get('item_text', '')
        Item.objects.create(text=new_text)
        return redirect('/')
    else:
        new_text = ''
    context = {
        'new_item_text': new_text
    }
    return render(request, 'home.html', context)