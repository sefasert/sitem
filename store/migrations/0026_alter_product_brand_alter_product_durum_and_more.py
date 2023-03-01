# Generated by Django 4.1.7 on 2023-02-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_product_brand_alter_product_ekran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Acer', 'acer'), ('Vestel-ALBA', 'vestel-alba'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Next', 'next'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('SHARP', 'sharp'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Hisense', 'hisense'), ('Skytech', 'skytech'), ('Panasonic', 'panasonic'), ('Vestel', 'vestel'), ('DARFON', 'darfon'), ('SONY', 'sony'), ('BOE', 'boe'), ('SUNNY', 'sunny'), ('ONVO', 'onvo'), ('Osawa', 'osawa'), ('REGAL', 'regal'), ('Premier', 'premier'), ('AXEN', 'axen'), ('SAMSUNG', 'samsung'), ('GEEPAS', 'geepas'), ('INNOLUX', 'innolux'), ('Vestel-SEG', 'vestel-seg'), ('Profilo', 'profilo'), ('NEXT', 'next'), ('YUMATU', 'yumatu'), ('CHIMEI', 'chimei'), ('AUO', 'auo'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Nordmende', 'nordmende'), ('SUNNY-AXEN', 'sunny-axen'), ('PHILIPS', 'philips'), ('Dijitsu', 'dijitsu'), ('Dreamstar', 'dreamstar'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SEG', 'seg'), ('LG', 'lg'), ('-', ''), ('Lifemaxx', 'lifemaxx'), ('Navitech', 'navitech'), ('SANYO', 'sanyo'), ('Homstar', 'homstar'), ('AWOX', 'awox'), ('ROWELL', 'rowell'), ('Vestel-Regal', 'vestel-regal'), ('MEGMEET', 'megmeet'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Hi-Level', 'hi-level'), ('WOON', 'woon')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED', 'led'), ('Plazma', 'plazma'), ('LCD', 'lcd'), ('LED-LCD', 'led-lcd')], max_length=10),
        ),
    ]
