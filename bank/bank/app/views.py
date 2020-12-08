from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from bank.app.forms.register import RegisterForm
from bank.app.forms.profile import ProfileForm


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


# Profile user view
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')

            if email != request.user.email:
                user = request.user
                user.email = email

                user.save()
                update_session_auth_hash(request, user)

                return redirect('index')
    else:
        form = ProfileForm()

    return render(request, 'app/user/profile.html', {'form': form, 'request': request})
