import requests
from bs4 import BeautifulSoup
from .models import Weather

from googletrans import Translator

def fetch_weather_data():
    url = 'https://obhavo.uz/tashkent' 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Failed to fetch data, status code: {response.status_code}"

    soup = BeautifulSoup(response.text, 'html.parser')
    
    translator = Translator()

    city = soup.find('h2').text.strip()
    city_en1 = translator.translate(city, src='uz', dest='en')
    city_en = city_en1.text
    city_uz = city
    city_ru1 = translator.translate(city, src='uz', dest='ru')
    city_ru = city_ru1.text

    date = soup.find('div', class_='current-day').text.strip()
    date_en1 = translator.translate(date, src='uz', dest='en')
    date_en = date_en1.text
    date_uz = date
    date_ru1 = translator.translate(date, src='uz', dest='ru')
    date_ru = date_ru1.text
    
    desk = soup.find('div', class_='current-forecast-desc').text.strip()
    desk_en1 = translator.translate(desk, src='uz', dest='en')
    desk_en = desk_en1.text
    desk_uz = desk
    desk_ru1 = translator.translate(desk, src='uz', dest='ru')
    desk_ru = desk_ru1.text
    

    current_temp = soup.find('div', class_='current-forecast').find('strong').text.strip()
    current_temp2 = soup.find('div', class_='current-forecast').find_all('span')[2].text.strip()

    humidity = soup.find('div', class_='col-1').find_all('p')[0].text.split(':')[1].strip()
    pressure = soup.find('div', class_='col-1').find_all('p')[2].text.split(':')[1].strip()

    sunrise1 = soup.find('div', class_='col-2').find_all('p')[1].text.split(':')[1].strip()
    sunrise2 = soup.find('div', class_='col-2').find_all('p')[1].text.split(':')[2].strip()
    sunset1 = soup.find('div', class_='col-2').find_all('p')[2].text.split(':')[1].strip()
    sunset2 = soup.find('div', class_='col-2').find_all('p')[2].text.split(':')[2].strip()
    
    forecast_divs = soup.find_all('div', class_='current-forecast-day')
    morning_temp = forecast_divs[0].find('div', class_='col-1').find(class_='forecast').text.strip()
    day_temp = forecast_divs[0].find('div', class_='col-2').find(class_='forecast').text.strip()
    evening_temp = forecast_divs[0].find('div', class_='col-3').find(class_='forecast').text.strip()
    
    
    try:
        Weather.objects.create(
            city = city,
            city_en = city_en,
            city_uz = city_uz,
            city_ru = city_ru,
            date = date,
            date_en = date_en,
            date_uz = date_uz,
            date_ru = date_ru,
            current_temp = current_temp,
            current_temp2 = current_temp2,
            desk = desk,
            desk_en = desk_en,
            desk_uz = desk_uz,
            desk_ru = desk_ru,
            humidity = humidity,
            pressure = pressure,
            sunrise1 = sunrise1,
            sunrise2 = sunrise2,
            sunset1 = sunset1,
            sunset2 = sunset2,
            morning_temp = morning_temp,
            day_temp = day_temp,
            evening_temp = evening_temp
            
        )
    except:
        pass
    
    return {
        'city': city,
        'date': date,
        'current_temp': current_temp,
        'desk': desk,
        'humidity': humidity,
        'pressure': pressure,
        'sunrise1': sunrise1,
        'sunrise2': sunrise2,
        'sunset1': sunset1,
        'sunset2': sunset2
    }




