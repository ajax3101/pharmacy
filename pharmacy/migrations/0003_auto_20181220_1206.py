# Generated by Django 2.1.3 on 2018-12-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_auto_20181206_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmgroup',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]