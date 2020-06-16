from django.contrib import admin

from .models import *

# Make admin classes here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profession', 'phone']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'program_name', 'branch']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'experience', 'organisation']

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'locality', 'city', 'state']

# Register your models here.

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Skills)
