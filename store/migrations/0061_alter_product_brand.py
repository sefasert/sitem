# Generated by Django 4.1.3 on 2023-02-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0060_alter_product_brand_alter_product_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('AUO', 'auo'), ('SEG', 'seg'), ('Acer', 'acer'), ('AWOX', 'awox'), ('Panasonic', 'panasonic'), ('Nordmende', 'nordmende'), ('SAMSUNG', 'samsung'), ('SANYO', 'sanyo'), ('SUNNY', 'sunny'), ('Premier', 'premier'), ('ROWELL', 'rowell'), ('Vestel-Regal', 'vestel-regal'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('YUMATU', 'yumatu'), ('Next', 'next'), ('WOON', 'woon'), ('Navitech', 'navitech'), ('Homstar', 'homstar'), ('Vestel', 'vestel'), ('NEXT', 'next'), ('SHARP', 'sharp'), ('Profilo', 'profilo'), ('Hisense', 'hisense'), ('SONY', 'sony'), ('Vestel-SEG', 'vestel-seg'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Dijitsu', 'dijitsu'), ('BOE', 'boe'), ('RONAX', 'ronax'), ('PHILIPS', 'philips'), ('SUNNY-AXEN', 'sunny-axen'), ('Skytech', 'skytech'), ('REGAL', 'regal'), ('LG', 'lg'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Hi-Level', 'hi-level'), ('Dreamstar', 'dreamstar'), ('Osawa', 'osawa'), ('GEEPAS', 'geepas'), ('Vestel-ALBA', 'vestel-alba'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('-', ''), ('Lifemaxx', 'lifemaxx'), ('ONVO', 'onvo'), ('AXEN', 'axen'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig')], max_length=100, null=True),
        ),
    ]
