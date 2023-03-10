# Generated by Django 4.1.7 on 2023-03-05 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_product_images3_product_webp3_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='webp3',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Hisense', 'hisense'), ('Lifemaxx', 'lifemaxx'), ('Navitech', 'navitech'), ('NEXT', 'next'), ('-', ''), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SONY', 'sony'), ('Dreamstar', 'dreamstar'), ('PHILIPS', 'philips'), ('SANYO', 'sanyo'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Vestel-Regal', 'vestel-regal'), ('SHARP', 'sharp'), ('Homstar', 'homstar'), ('Premier', 'premier'), ('Acer', 'acer'), ('Nordmende', 'nordmende'), ('AWOX', 'awox'), ('Next', 'next'), ('Hi-Level', 'hi-level'), ('LG', 'lg'), ('Osawa', 'osawa'), ('REGAL', 'regal'), ('SUNNY', 'sunny'), ('AXEN', 'axen'), ('YUMATU', 'yumatu'), ('SUNNY-AXEN', 'sunny-axen'), ('AUO', 'auo'), ('WOON', 'woon'), ('Vestel-SEG', 'vestel-seg'), ('Skytech', 'skytech'), ('CHIMEI', 'chimei'), ('GEEPAS', 'geepas'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Vestel-ALBA', 'vestel-alba'), ('Panasonic', 'panasonic'), ('SAMSUNG', 'samsung'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Dijitsu', 'dijitsu'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Profilo', 'profilo'), ('MEGMEET', 'megmeet'), ('ONVO', 'onvo'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('BOE', 'boe'), ('SEG', 'seg'), ('ROWELL', 'rowell'), ('Vestel', 'vestel'), ('INNOLUX', 'innolux'), ('DARFON', 'darfon'), ('Vestel, Hi-Level', 'vestel,hi-level')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED-LCD', 'led-lcd'), ('LCD', 'lcd'), ('Plazma', 'plazma'), ('LED', 'led')], max_length=10),
        ),
    ]
