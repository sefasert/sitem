# Generated by Django 4.1.7 on 2023-02-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Panasonic', 'panasonic'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Homstar', 'homstar'), ('YUMATU', 'yumatu'), ('SAMSUNG', 'samsung'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Vestel-ALBA', 'vestel-alba'), ('Skytech', 'skytech'), ('-', ''), ('AUO', 'auo'), ('Hi-Level', 'hi-level'), ('GEEPAS', 'geepas'), ('DARFON', 'darfon'), ('Vestel', 'vestel'), ('AXEN', 'axen'), ('Premier', 'premier'), ('ROWELL', 'rowell'), ('Vestel-SEG', 'vestel-seg'), ('Acer', 'acer'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Dijitsu', 'dijitsu'), ('BOE', 'boe'), ('AWOX', 'awox'), ('Osawa', 'osawa'), ('CHIMEI', 'chimei'), ('SUNNY', 'sunny'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('PHILIPS', 'philips'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Vestel-Regal', 'vestel-regal'), ('NEXT', 'next'), ('ONVO', 'onvo'), ('Hisense', 'hisense'), ('INNOLUX', 'innolux'), ('SONY', 'sony'), ('Nordmende', 'nordmende'), ('Next', 'next'), ('SANYO', 'sanyo'), ('Dreamstar', 'dreamstar'), ('SHARP', 'sharp'), ('SEG', 'seg'), ('Navitech', 'navitech'), ('REGAL', 'regal'), ('MEGMEET', 'megmeet'), ('Profilo', 'profilo'), ('Lifemaxx', 'lifemaxx'), ('LG', 'lg'), ('RONAX-TELENOVA', 'ronax-telenova'), ('WOON', 'woon'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SUNNY-AXEN', 'sunny-axen')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED', 'led'), ('LCD', 'lcd'), ('LED-LCD', 'led-lcd'), ('Plazma', 'plazma')], max_length=10),
        ),
    ]
