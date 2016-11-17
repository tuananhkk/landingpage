from django.conf.urls import include, url
from django.contrib import admin

#import view list for link
from .views import (
	contact,
    )

urlpatterns = [
    url(r'^$', contact, name = 'contact'),
]