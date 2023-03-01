# Generated by Django 4.1.7 on 2023-02-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_alter_product_brand_alter_product_ekran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SUNNY-AXEN', 'sunny-axen'), ('INNOLUX', 'innolux'), ('ROWELL', 'rowell'), ('-', ''), ('DARFON', 'darfon'), ('NEXT', 'next'), ('Skytech', 'skytech'), ('Hi-Level', 'hi-level'), ('Next', 'next'), ('REGAL', 'regal'), ('AXEN', 'axen'), ('CHIMEI', 'chimei'), ('Navitech', 'navitech'), ('SANYO', 'sanyo'), ('Profilo', 'profilo'), ('SONY', 'sony'), ('BOE', 'boe'), ('Osawa', 'osawa'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Vestel-Regal', 'vestel-regal'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SAMSUNG', 'samsung'), ('Premier', 'premier'), ('Nordmende', 'nordmende'), ('WOON', 'woon'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Acer', 'acer'), ('AUO', 'auo'), ('MEGMEET', 'megmeet'), ('ONVO', 'onvo'), ('SHARP', 'sharp'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Dreamstar', 'dreamstar'), ('PHILIPS', 'philips'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Vestel-SEG', 'vestel-seg'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('LG', 'lg'), ('Vestel-ALBA', 'vestel-alba'), ('Vestel', 'vestel'), ('YUMATU', 'yumatu'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Dijitsu', 'dijitsu'), ('SEG', 'seg'), ('AWOX', 'awox'), ('GEEPAS', 'geepas'), ('Panasonic', 'panasonic'), ('SUNNY', 'sunny'), ('Lifemaxx', 'lifemaxx'), ('Hisense', 'hisense'), ('Homstar', 'homstar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED', 'led'), ('LED-LCD', 'led-lcd'), ('LCD', 'lcd'), ('Plazma', 'plazma')], max_length=10),
        ),
    ]
