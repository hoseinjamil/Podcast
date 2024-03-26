from django.shortcuts import render
from .models import Contactme
from .forms import *
from django.contrib import messages



def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            Contactme.objects.create(first_name=first_name, last_name=last_name, email=email, subject=subject, body=body)
            messages.success(request, "Your message has been sent")
            return render(request, 'contact/contact.html', context={'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', context={'form': form})
