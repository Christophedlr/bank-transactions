from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from bank.app.forms.register import RegisterForm
from bank.app.forms.profile import ProfileForm, ChangePasswordForm


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
        form2 = ChangePasswordForm(request.POST)

        if "email_form" in request.POST and form.is_valid():
            email = form.cleaned_data.get('email')

            if email != request.user.email:
                user = request.user
                user.email = email

                user.save()
                update_session_auth_hash(request, user)

                return redirect('index')
        elif "password_form" in request.POST and form2.is_valid():
            password1 = form2.cleaned_data.get('password1')
            password2 = form2.cleaned_data.get('password2')

            if password1 == password2:
                user = request.user
                user.set_password(password1)

                user.save()
                update_session_auth_hash(request, user)

                return redirect('index')
    else:
        form = ProfileForm()
        form2 = ChangePasswordForm()

    return render(request, 'app/user/profile.html', {'form': form, 'form2': form2, 'request': request})
