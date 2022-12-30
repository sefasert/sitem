# Generated by Django 4.1.3 on 2022-12-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_product_brand_alter_product_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SANYO', 'sanyo'), ('PHILIPS', 'philips'), ('Panasonic', 'panasonic'), ('LG', 'lg'), ('Next', 'next'), ('Navitech', 'navitech'), ('Botech', 'botech'), ('AXEN', 'axen'), ('CVS', 'cvs'), ('Profilo', 'profilo'), ('-', ''), ('Nordmende', 'nordmende'), ('ONVO', 'onvo'), ('Homstar', 'homstar'), ('AWOX', 'awox'), ('Lifemaxx', 'lifemaxx'), ('SAMSUNG', 'samsung'), ('SUNNY', 'sunny'), ('GEEPAS', 'geepas'), ('VESTEL', 'vestel'), ('Skytech', 'skytech'), ('SONY', 'sony'), ('YUMATU', 'yumatu'), ('Osawa', 'osawa'), ('Dreamstar', 'dreamstar'), ('Premier', 'premier'), ('NEXT', 'next'), ('TOSHIBA', 'toshiba'), ('ROWELL', 'rowell'), ('SUNNY-AXEN', 'sunny-axen'), ('Dijitsu', 'dijitsu'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50, null=True),
        ),
    ]