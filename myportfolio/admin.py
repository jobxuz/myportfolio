from django.contrib import admin
from .models import About, Contact, Contacturl, Skills,Weather, Prayer, RamadanCalendar, Region
from modeltranslation.admin import TranslationAdmin



# @admin.register(About)
# class AboutAdmin(TranslationAdmin):
#     pass



admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Contacturl)
admin.site.register(Skills)
admin.site.register(Weather)
admin.site.register(Prayer)
admin.site.register(Region)
admin.site.register(RamadanCalendar)
