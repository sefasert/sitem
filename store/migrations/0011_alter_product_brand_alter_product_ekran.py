# Generated by Django 4.1.7 on 2023-02-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Dijitsu', 'dijitsu'), ('Vestel-ALBA', 'vestel-alba'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('BOE', 'boe'), ('Lifemaxx', 'lifemaxx'), ('Profilo', 'profilo'), ('SHARP', 'sharp'), ('AWOX', 'awox'), ('Premier', 'premier'), ('SAMSUNG', 'samsung'), ('Hi-Level', 'hi-level'), ('DARFON', 'darfon'), ('SUNNY-AXEN', 'sunny-axen'), ('SEG', 'seg'), ('Skytech', 'skytech'), ('REGAL', 'regal'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Navitech', 'navitech'), ('Vestel-Regal', 'vestel-regal'), ('Nordmende', 'nordmende'), ('SONY', 'sony'), ('Dreamstar', 'dreamstar'), ('Panasonic', 'panasonic'), ('RONAX-TELENOVA', 'ronax-telenova'), ('PHILIPS', 'philips'), ('Homstar', 'homstar'), ('YUMATU', 'yumatu'), ('Next', 'next'), ('ROWELL', 'rowell'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('SANYO', 'sanyo'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('WOON', 'woon'), ('GEEPAS', 'geepas'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('ONVO', 'onvo'), ('MEGMEET', 'megmeet'), ('NEXT', 'next'), ('INNOLUX', 'innolux'), ('AUO', 'auo'), ('LG', 'lg'), ('SUNNY', 'sunny'), ('Hisense', 'hisense'), ('CHIMEI', 'chimei'), ('Vestel-SEG', 'vestel-seg'), ('Osawa', 'osawa'), ('Vestel', 'vestel'), ('-', ''), ('Acer', 'acer'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('AXEN', 'axen')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED-LCD', 'led-lcd'), ('LCD', 'lcd'), ('LED', 'led'), ('Plazma', 'plazma')], max_length=10),
        ),
    ]
