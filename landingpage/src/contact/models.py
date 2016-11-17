from django.db import models

from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 255, blank=False, verbose_name = "Full Name")
    email = models.EmailField(blank=False, verbose_name = "Email")
    phone = PhoneNumberField(blank=False, verbose_name = "Phone Number")
    content = models.TextField(max_length = 150, verbose_name = "Request Details")
    timestamp = models.DateTimeField(auto_now_add = True, verbose_name = "Request Time")
    
    def __str__(self):
        return self.name + " - " + self.id
    
    # def get_absolute_url(self):
        # return reverse()
    class Meta:
        ordering = ["-timestamp"]
    