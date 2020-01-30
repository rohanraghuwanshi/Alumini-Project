from django.contrib import admin

from .models import Profile, CollegeDetails

# Make admin classes here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profession', 'phone']

class CollegeDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'course_name', 'branch', 'batch']



# Register your models here.

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CollegeDetails, CollegeDetailsAdmin)