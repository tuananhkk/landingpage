from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact(request):
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
    else:
        form = ContactForm()
    
    context = {
	    "form": form
	}
	
    return render(request, 'base.html', context)