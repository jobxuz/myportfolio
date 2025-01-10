import requests
from bs4 import BeautifulSoup
from .models import Prayer


def nomozdata():
    url = 'https://namozvaqti.uz/shahar/toshkent'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return f"Failed to fetch data, status code: {response.status_code}"

    soup = BeautifulSoup(response.text, 'html.parser')
    
    namoz_vaqtlari = []
    ad_items = soup.find_all('div', class_='ad__item')

    for item in ad_items:
        time = item.find('p', class_='time').text.strip()
        name = item.find('h2', class_='nam').text.strip()
        namoz_vaqtlari.append({'nom': name, 'vaqt': time})
        
        
    # for namoz in namoz_vaqtlari:
    #     print(f"{namoz['nom']}: {namoz['vaqt']}")
        
    Prayer.objects.create(
        bomdod = namoz_vaqtlari[0]['vaqt'],
        quyosh = namoz_vaqtlari[1]['vaqt'],
        peshin = namoz_vaqtlari[2]['vaqt'],
        asr = namoz_vaqtlari[3]['vaqt'],
        shom = namoz_vaqtlari[4]['vaqt'],
        xufton = namoz_vaqtlari[5]['vaqt']
    )
        
    
    return namoz_vaqtlari




    
    
    