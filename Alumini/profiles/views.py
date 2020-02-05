from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import UserRegistrationForm

# Create your views here.

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm

    template_name = "registration/registration.html"

    def form_valid(self, form):
        if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            # login(self.request, new_user)
            return redirect('/register/add-profile-picture')
        else:
            return super().form_valid(form)
