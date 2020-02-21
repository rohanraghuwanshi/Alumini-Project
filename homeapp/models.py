from django.db import models
from django.shortcuts import redirect

# Create your models here.

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
