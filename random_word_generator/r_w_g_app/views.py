from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 1
    else:
        request.session['attempts'] += 1
    
    context = {
    'randnum' : get_random_string(length=14)
    }
    
    return render(request,'index.html',context)

def reset(request):
    request.session.flush()
    return redirect("/")