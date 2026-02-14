from django.shortcuts import render
from .models import About, Contact, Contacturl, RamadanCalendar, Region, Skills, Weather, Prayer
from datetime import date




def indexview(request):
    about = About.objects.last()
    contacturl = Contacturl.objects.all()
    skills = Skills.objects.all()
    weather = Weather.objects.last()
    prayer = Prayer.objects.last()
    contact = Contact.objects.last()

    regions = Region.objects.all()
    region_id = request.GET.get("region")

    if region_id:
        selected_region = Region.objects.filter(id=region_id).first()
    else:
        selected_region = regions.first()

    if selected_region:
        ramadan_days = RamadanCalendar.objects.filter(
            region=selected_region
        ).order_by("day")
    else:
        ramadan_days = []

    today = date.today()

    return render(request, 'index.html', {
        'about': about,
        'contacturl': contacturl,
        'skills': skills,
        'weather': weather,
        'prayer': prayer,
        'contact': contact,
        'regions': regions,
        'selected_region': selected_region,
        'ramadan_days': ramadan_days,
        'today': today,
    })
