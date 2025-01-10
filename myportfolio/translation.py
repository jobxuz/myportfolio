from modeltranslation.translator import translator, TranslationOptions
from .models import About, Contact, Weather

class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'deskription') 


class ContactTranslationOptions(TranslationOptions):
    fields = ('addres', 'email') 



class WeatherTranslationOptions(TranslationOptions):
    fields = ('city', 'date', 'desk') 


translator.register(About, AboutTranslationOptions),
translator.register(Contact, ContactTranslationOptions),
translator.register(Weather, WeatherTranslationOptions)
