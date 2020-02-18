from django.contrib import admin

from .models import ContactRequest

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


# Register your models here.
admin.site.register(ContactRequest, ContactRequestAdmin)