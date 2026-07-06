from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        # Bootstrap styling
        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })

        form.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password'
        })

        form.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

        if form.is_valid():

            user = form.save()

            Profile.objects.create(user=user)

            return redirect('login')

    else:

        form = UserCreationForm()

        # Bootstrap styling
        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })

        form.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password'
        })

        form.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        # Bootstrap styling
        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })

        form.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('feed')

    else:

        form = AuthenticationForm()

        # Bootstrap styling
        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })

        form.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })

    return render(
        request,
        'accounts/login.html',
        {
            'form': form
        }
    )


def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def profile(request):

    profile = Profile.objects.get(user=request.user)

    return render(
        request,
        'accounts/profile.html',
        {
            'profile': profile
        }
    )