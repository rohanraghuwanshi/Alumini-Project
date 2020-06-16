from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView

from .forms import *
from .models import *
from homeapp.models import FooterAboutus

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
            new_user = authenticate(
                            username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                        )
            login(self.request, new_user)
            return redirect('/accounts/registration/add-profile-picture')
        else:
            return super().form_valid(form)

class ProfilePictureUploadView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfilePictureForm

    template_name = "registration/profilepic_upload.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/accounts/registration/complete-profile/'+str(self.request.user.profile.id))

class ProfileCompletionView(UpdateView):
    model = Profile
    form_class = ProfileCompletionForm

    template_name = "registration/profile_complete.html"

    def form_valid(self, form):
        form.save()
        return redirect('/accounts/registration/add-address/')

class AddressView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm

    template_name = "registration/address.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/accounts/registration/add-profile-links/'+str(self.request.user.profile.id))

class ProfileLinkAdditionView(UpdateView):
    model = Profile
    form_class = ProfileLinksForm

    template_name = "registration/profile_links.html"

    def form_valid(self, form):
        form.save()
        return redirect('/')

class ProfileView(DetailView):
    model = Profile
    template_name = "registration/profilepage.htm"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['footer'] = FooterAboutus.objects.all()[0]
        context['experiences'] = Experience.objects.all().filter(user=self.kwargs['pk'])
        context['education'] = Education.objects.all().filter(user=self.kwargs['pk'])
        context['achievements'] = Achievement.objects.all().filter(user=self.kwargs['pk'])
        context['skills'] = Skills.objects.all().filter(user=self.kwargs['pk'])
        return context