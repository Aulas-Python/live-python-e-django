from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def meu_login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_authenticated = authenticate(username=user, password=password)

            login(request, user_authenticated)

            return redirect('/blog/')


    context = {
        'form': form
    }

    return render(request, 'login.html', context=context)