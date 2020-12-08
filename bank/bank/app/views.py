from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from bank.app.forms.register import RegisterForm


def index(request):
    return render(request, 'app/index.html', {'request': request})


# Registration user view
def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.is_active = False
            user_form.save()

            return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'app/user/register.html', {'form': form})
