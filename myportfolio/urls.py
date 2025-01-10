from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import indexview
#from django.views.i18n import set_language




urlpatterns =(
    path('', indexview, name='home'),
    #path('set_language/', set_language, name='set_language'),
    
)