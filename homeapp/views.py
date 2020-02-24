from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .models import ContactRequest
from .forms import ContactRequestForm
# Create your views here.

class IndexView(TemplateView):
    template_name = "homeapp/index.html"

class AboutusView(TemplateView):
    template_name = "homeapp/aboutus.html"

class ContactRequestView(CreateView):
    model = ContactRequest
    form_class = ContactRequestForm

    template_name = "homeapp/contact.html"

    def form_invalid(self, form):
        form.save()
        return redirect('/')