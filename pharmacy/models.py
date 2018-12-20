from django.db import models
from django.contrib.auth.models import User
#from django_countries.fields import CountryField

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
   
    def __str__(self):
        return self.name  

class PharmGroup(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    descr = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    member = models.CharField(max_length=100, verbose_name='Представитель')
    position = models.CharField(max_length=100, verbose_name='Должность')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='Страна')
    #country = CountryField()
    phone_m = models.CharField(max_length=100, verbose_name='Контактный телефон')
    descr = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.name

class Pharmacy(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pharmacy')
    name = models.CharField(max_length=100, verbose_name='Название Аптеки')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    adress = models.CharField(max_length=100, verbose_name='Адрес Аптеки')
    logo = models.ImageField(upload_to='pharmacy_logo/', blank=False)

    def __str__(self):
        return self.name

class Drug(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    pharmgroup = models.ForeignKey(PharmGroup, on_delete=models.CASCADE)
    drug_id = models.CharField(max_length=30, verbose_name='Номер')
    name = models.CharField(max_length=30, verbose_name='Название')
    inter_name = models.CharField(max_length=30, verbose_name='Международное название')
    short_descr = models.TextField(verbose_name='Формы выпуска')
    con_pack_codes = models.TextField(verbose_name='Штрих-коды потребительской упаковки')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drug_images/', blank=False)
    data = models.DateField(verbose_name='Дата препарата')
    data_exp = models.DateField(verbose_name='Срок годности')
    quantity = models.IntegerField(verbose_name='Количество')
    price_buy = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена закупки')
    price_sell = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена продажи')
    
    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.get_full_name()
   