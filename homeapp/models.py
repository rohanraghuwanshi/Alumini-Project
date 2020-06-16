from django.db import models
from django.shortcuts import redirect

# Create your models here.
class Slider(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="slider_images")
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.name


class HomeAboutUs(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = "HomeAboutUs"
        verbose_name_plural = "HomeAboutUss"

    def __str__(self):
        return self.name


class HomepageMessage(models.Model):

    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    message = models.TextField()

    image = models.ImageField(upload_to="HomeMessageImages")

    class Meta:
        verbose_name = "HomepageMessage"
        verbose_name_plural = "HomepageMessages"

    def __str__(self):
        return self.name


class FooterAboutus(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()
    contact = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    location = models.TextField()
    location_link = models.TextField(default='https://g.page/medi-caps-university-indore?share')


    class Meta:
        verbose_name = "FooterAboutus"
        verbose_name_plural = "FooterAboutus"

    def __str__(self):
        return self.name


class ContactRequest(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10, blank=True, null=True)
    text = models.TextField()

    class Meta:
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"

    def __str__(self):
        return self.name
