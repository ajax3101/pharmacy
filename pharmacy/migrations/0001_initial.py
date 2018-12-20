# Generated by Django 2.1.3 on 2018-12-03 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название Аптеки')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('adress', models.CharField(max_length=100, verbose_name='Адрес Аптеки')),
                ('logo', models.ImageField(upload_to='pharmacy_logo/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]