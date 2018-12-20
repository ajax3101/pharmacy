# Generated by Django 2.1.3 on 2018-12-06 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_id', models.CharField(max_length=30, verbose_name='Номер')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('inter_name', models.CharField(max_length=30, verbose_name='Международное название')),
                ('short_descr', models.TextField(verbose_name='Формы выпуска')),
                ('con_pack_codes', models.TextField(verbose_name='Штрих-коды потребительской упаковки')),
                ('image', models.ImageField(upload_to='drug_images/')),
                ('data', models.DateField(verbose_name='Дата препарата')),
                ('data_exp', models.DateField(verbose_name='Срок годности')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('price_buy', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена закупки')),
                ('price_sell', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена продажи')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('member', models.CharField(max_length=100, verbose_name='Представитель')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('phone_m', models.CharField(max_length=100, verbose_name='Контактный телефон')),
                ('descr', models.TextField(verbose_name='Описание')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Страна', to='pharmacy.Country')),
            ],
        ),
        migrations.CreateModel(
            name='PharmGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('descr', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Manufacturer'),
        ),
        migrations.AddField(
            model_name='drug',
            name='pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Pharmacy'),
        ),
        migrations.AddField(
            model_name='drug',
            name='pharmgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.PharmGroup'),
        ),
    ]