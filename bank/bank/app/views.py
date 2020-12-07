from django.shortcuts import render
from .forms.login import LoginForm


def index(request):
    return render(request, 'app/index.html', {})


# Login form
def login(request):
    form = LoginForm();
    return render(request, 'app/user/login.html', {'form': form})
