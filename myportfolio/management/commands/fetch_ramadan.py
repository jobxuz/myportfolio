import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.core.management.base import BaseCommand

from myportfolio.models import RamadanCalendar, Region


REGIONS = [
    ("Toshkent shahri", "toshkent"),
    ("Samarqand", "samarqand"),
    ("Buxoro", "buxoro"),
    ("Navoiy", "navoiy"),
    ("Andijon", "andijon"),
    ("Namangan", "namangan"),
    ("Fargona", "fargona"),
    ("Jizzax", "jizzax"),
    ("Sirdaryo", "sirdaryo"),
    ("Qashqadaryo", "qarshi"),
    ("Surxondaryo", "termiz"),
    ("Xorazm", "urganch"),
    ("Qoraqalpogiston", "nukus"),
]


UZ_MONTHS = {
    "Yanvar": "January",
    "Fevral": "February",
    "Mart": "March",
    "Aprel": "April",
    "May": "May",
}


class Command(BaseCommand):
    help = "Fetch Ramadan calendar for all 14 regions"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🚀 Ramazon taqvimi yuklanmoqda..."))

        # Regionlarni yaratish
        for name, slug in REGIONS:
            Region.objects.get_or_create(name=name, slug=slug)

        regions = Region.objects.all()

        for region in regions:
            self.fetch_region(region)

        self.stdout.write(self.style.SUCCESS("✅ Barcha viloyatlar saqlandi."))

    def fetch_region(self, region):
        url = f"https://namozvaqti.uz/ramazon/{region.slug}"
        print(f"url: {url}")
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"{region.name} yuklanmadi"))
            return

        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", class_="table_calendar")

        if not table:
            self.stdout.write(self.style.ERROR(f"{region.name} jadval topilmadi"))
            return

        rows = table.find_all("tr")[1:]

        saved = 0

        for row in rows:
            cols = row.find_all("td")

            if len(cols) < 5:
                continue

            day = int(cols[0].text.strip())
            week_day = cols[1].text.strip()
            date_text = cols[2].text.strip()
            saharlik = cols[3].text.strip()
            iftorlik = cols[4].text.strip()

            # Oy nomlarini inglizchaga o'tkazish
            for uz, en in UZ_MONTHS.items():
                date_text = date_text.replace(uz, en)

            date_obj = datetime.strptime(date_text, "%d %B %Y").date()

            RamadanCalendar.objects.update_or_create(
                region=region,
                day=day,
                date=date_obj,
                defaults={
                    "week_day": week_day,
                    "saharlik": saharlik,
                    "iftorlik": iftorlik,
                }
            )

            saved += 1

        self.stdout.write(
            self.style.SUCCESS(f"{region.name} → {saved} kun saqlandi")
        )
