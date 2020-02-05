from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    profilepic = models.ImageField(default='Pictures/profile_pics/default.png', upload_to='Pictures/profile_pics', blank='true')

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return str(self.user)

class Education(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    program_name = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return str(self.user)

class Skills(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Skills"
        verbose_name_plural = "Skills"

    def __str__(self):
        return str(self.user)

class Experience(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return str(self.user)

class Achievement(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return str(self.user)

class Testimonial(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimonial_from = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    testimonial_desc = models.TextField()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return str(self.user)