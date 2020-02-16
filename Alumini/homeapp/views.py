from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "homeapp/index.html"

class AboutusView(TemplateView):
    template_name = "homeapp/aboutus.html"

class ContactView(TemplateView):
    template_name = "homeapp/contact.html"

