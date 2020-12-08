from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms.login import LoginForm


def index(request):
    return render(request, 'app/index.html', {'request': request})


# Login form
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

    form = LoginForm()
    return render(request, 'app/user/login.html', {'form': form})
