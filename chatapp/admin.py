from django.contrib import admin

from .models import Message

# class ContactAdmin(admin.ModelAdmin):
    # list_display = ['user', 'friend']


# admin.site.register(Chat)
# admin.site.register(Contact, ContactAdmin)
admin.site.register(Message)
