from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .models import ContactRequest, Slider, HomeAboutUs, HomepageMessage, FooterAboutus
from .forms import ContactRequestForm
# Create your views here.

class IndexView(TemplateView):
    template_name = "homeapp/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['sliders'] = Slider.objects.all()
        context['aboutus'] = HomeAboutUs.objects.all()[:3]
        context['messages'] = HomepageMessage.objects.all()
        context['footer'] = FooterAboutus.objects.all()[0]
        return context

class AboutusView(TemplateView):
    template_name = "homeapp/aboutus.html"

class ContactRequestView(CreateView):
    model = ContactRequest
    form_class = ContactRequestForm

    template_name = "homeapp/contact.html"

    def form_invalid(self, form):
        form.save()
        return redirect('/')