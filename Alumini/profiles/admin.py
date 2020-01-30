from django.contrib import admin

from .models import *

# Make admin classes here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profession', 'phone']

class CollegeDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'program', 'branch', 'batch']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch', 'specialization']
    


# Register your models here.

admin.site.register(Program)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CollegeDetails, CollegeDetailsAdmin)
admin.site.register(Branch, BranchAdmin)
