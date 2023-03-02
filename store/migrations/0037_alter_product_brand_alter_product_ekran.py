# Generated by Django 4.1.7 on 2023-02-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('GEEPAS', 'geepas'), ('Hisense', 'hisense'), ('LG', 'lg'), ('Next', 'next'), ('YUMATU', 'yumatu'), ('MEGMEET', 'megmeet'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('SAMSUNG', 'samsung'), ('Panasonic', 'panasonic'), ('SEG', 'seg'), ('INNOLUX', 'innolux'), ('AUO', 'auo'), ('ONVO', 'onvo'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('ROWELL', 'rowell'), ('SANYO', 'sanyo'), ('Skytech', 'skytech'), ('AWOX', 'awox'), ('Homstar', 'homstar'), ('Dreamstar', 'dreamstar'), ('-', ''), ('NEXT', 'next'), ('SONY', 'sony'), ('Lifemaxx', 'lifemaxx'), ('DARFON', 'darfon'), ('AXEN', 'axen'), ('Vestel-ALBA', 'vestel-alba'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Hi-Level', 'hi-level'), ('CHIMEI', 'chimei'), ('BOE', 'boe'), ('Dijitsu', 'dijitsu'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Vestel', 'vestel'), ('Premier', 'premier'), ('WOON', 'woon'), ('Profilo', 'profilo'), ('PHILIPS', 'philips'), ('Navitech', 'navitech'), ('Vestel-Regal', 'vestel-regal'), ('Vestel-SEG', 'vestel-seg'), ('REGAL', 'regal'), ('SUNNY', 'sunny'), ('SUNNY-AXEN', 'sunny-axen'), ('Osawa', 'osawa'), ('SHARP', 'sharp'), ('Acer', 'acer'), ('Nordmende', 'nordmende')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED-LCD', 'led-lcd'), ('LED', 'led'), ('Plazma', 'plazma'), ('LCD', 'lcd')], max_length=10),
        ),
    ]