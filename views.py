from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/home')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})
