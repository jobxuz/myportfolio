from django.shortcuts import render
from .models import About, Contact, Contacturl, Skills, Weather, Prayer



def indexview(request):
    about = About.objects.last()
    contacturl = Contacturl.objects.all()
    skills = Skills.objects.all()
    weather = Weather.objects.last()
    prayer = Prayer.objects.last()
    contact = Contact.objects.last()
    
    
    return render(request, 'index.html', {
        'about':about, 
        'contacturl':contacturl, 
        'skills':skills,
        'weather':weather,
        'prayer':prayer,
        'contact':contact
        })