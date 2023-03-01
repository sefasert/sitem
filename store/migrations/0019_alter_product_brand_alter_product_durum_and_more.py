# Generated by Django 4.1.7 on 2023-02-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('DARFON', 'darfon'), ('Hi-Level', 'hi-level'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Skytech', 'skytech'), ('REGAL', 'regal'), ('AXEN', 'axen'), ('AWOX', 'awox'), ('Vestel', 'vestel'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('SAMSUNG', 'samsung'), ('RONAX-TELENOVA', 'ronax-telenova'), ('BOE', 'boe'), ('Vestel-ALBA', 'vestel-alba'), ('YUMATU', 'yumatu'), ('Hisense', 'hisense'), ('SANYO', 'sanyo'), ('Acer', 'acer'), ('Vestel-SEG', 'vestel-seg'), ('SEG', 'seg'), ('PHILIPS', 'philips'), ('MEGMEET', 'megmeet'), ('ROWELL', 'rowell'), ('Navitech', 'navitech'), ('Lifemaxx', 'lifemaxx'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('-', ''), ('SUNNY', 'sunny'), ('GEEPAS', 'geepas'), ('Dijitsu', 'dijitsu'), ('AUO', 'auo'), ('Osawa', 'osawa'), ('ONVO', 'onvo'), ('INNOLUX', 'innolux'), ('Next', 'next'), ('SHARP', 'sharp'), ('Vestel-Regal', 'vestel-regal'), ('Dreamstar', 'dreamstar'), ('WOON', 'woon'), ('Panasonic', 'panasonic'), ('Nordmende', 'nordmende'), ('SONY', 'sony'), ('Homstar', 'homstar'), ('LG', 'lg'), ('SUNNY-AXEN', 'sunny-axen'), ('Premier', 'premier'), ('CHIMEI', 'chimei'), ('Profilo', 'profilo'), ('NEXT', 'next'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('Plazma', 'plazma'), ('LED', 'led'), ('LED-LCD', 'led-lcd'), ('LCD', 'lcd')], max_length=10),
        ),
    ]
