from celery import shared_task
from .weather import fetch_weather_data
from .prayer_time import nomozdata




@shared_task
def weather_task():
    fetch_weather_data()
    
    return 'Temperatura qushildi!!'
    


@shared_task
def prayer_task():
    nomozdata()
    
    return 'Nomoz vaqtlari qushildi!!'


#      celery -A core worker --loglevel=info --pool=solo
#      celery -A core beat --loglevel=info
