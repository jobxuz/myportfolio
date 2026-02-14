from django.db import models


class About(models.Model):
    name = models.CharField(max_length=100)
    deskription = models.TextField()
    img = models.ImageField(upload_to='img/')
    
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    addres = models.CharField(max_length=250)
    cv = models.FileField(upload_to='img/', null=True, blank=True)
    
    
    def __str__(self):
        return self.phone
    
    
class Contacturl(models.Model):
    name = models.CharField(max_length=100)
    contacturl = models.URLField(max_length=250)
    
    
    def __str__(self):
        return self.name
    
    
class Skills(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    

class Weather(models.Model):
    city = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    current_temp = models.CharField(max_length=100)
    current_temp2 = models.CharField(max_length=100, null=True, blank=True)
    desk = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    pressure = models.CharField(max_length=100)
    sunrise1 = models.CharField(max_length=100)
    sunrise2 = models.CharField(max_length=100)
    sunset1 = models.CharField(max_length=100)
    sunset2 = models.CharField(max_length=100)
    morning_temp = models.CharField(max_length=100, null=True, blank=True)
    day_temp = models.CharField(max_length=100, null=True, blank=True)
    evening_temp = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.city
    
    
    
class Prayer(models.Model):
    bomdod = models.CharField(max_length=100, null=True, blank=True)
    quyosh = models.CharField(max_length=100, null=True, blank=True)
    peshin = models.CharField(max_length=100, null=True, blank=True)
    asr = models.CharField(max_length=100, null=True, blank=True)
    shom = models.CharField(max_length=100, null=True, blank=True)
    xufton = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return f"Bomdod: {self.bomdod} | Peshin: {self.peshin} | Asr: {self.asr} | Shom: {self.shom} | Xufton: {self.xufton}"
    




class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



class RamadanCalendar(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="ramadan_days"
    )
    day = models.IntegerField()
    week_day = models.CharField(max_length=10)
    date = models.DateField()
    saharlik = models.TimeField()
    iftorlik = models.TimeField()

    class Meta:
        unique_together = ("region", "day", "date")
        ordering = ["region", "day"]

    def __str__(self):
        return f"{self.region.name} - {self.day}-kun"
