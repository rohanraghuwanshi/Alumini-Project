from django.contrib import admin

from .models import ContactRequest, Slider, HomeAboutUs, HomepageMessage, FooterAboutus

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


# Register your models here.
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(HomepageMessage)
admin.site.register(FooterAboutus)
admin.site.register(HomeAboutUs)
admin.site.register(Slider)