# Generated by Django 4.1.3 on 2023-02-03 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_alter_product_brand_alter_product_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Nordmende', 'nordmende'), ('ROWELL', 'rowell'), ('SUNNY-AXEN', 'sunny-axen'), ('Vestel-SEG', 'vestel-seg'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Profilo', 'profilo'), ('Dijitsu', 'dijitsu'), ('SANYO', 'sanyo'), ('WOON', 'woon'), ('Next', 'next'), ('AXEN', 'axen'), ('AUO', 'auo'), ('Panasonic', 'panasonic'), ('ONVO', 'onvo'), ('Vestel-Regal', 'vestel-regal'), ('GEEPAS', 'geepas'), ('SEG', 'seg'), ('Osawa', 'osawa'), ('AWOX', 'awox'), ('YUMATU', 'yumatu'), ('Premier', 'premier'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Homstar', 'homstar'), ('SONY', 'sony'), ('Hisense', 'hisense'), ('Lifemaxx', 'lifemaxx'), ('NEXT', 'next'), ('Navitech', 'navitech'), ('Vestel-ALBA', 'vestel-alba'), ('SAMSUNG', 'samsung'), ('RONAX', 'ronax'), ('Vestel', 'vestel'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SUNNY', 'sunny'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Hi-Level', 'hi-level'), ('PHILIPS', 'philips'), ('REGAL', 'regal'), ('Skytech', 'skytech'), ('BOE', 'boe'), ('-', ''), ('SHARP', 'sharp'), ('LG', 'lg'), ('Dreamstar', 'dreamstar'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal')], max_length=100, null=True),
        ),
    ]