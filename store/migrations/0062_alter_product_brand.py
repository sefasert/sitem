# Generated by Django 4.1.3 on 2023-02-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0061_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Dreamstar', 'dreamstar'), ('BOE', 'boe'), ('Vestel-SEG', 'vestel-seg'), ('LG', 'lg'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Osawa', 'osawa'), ('Dijitsu', 'dijitsu'), ('Vestel', 'vestel'), ('SANYO', 'sanyo'), ('YUMATU', 'yumatu'), ('Next', 'next'), ('Hisense', 'hisense'), ('ONVO', 'onvo'), ('SONY', 'sony'), ('AUO', 'auo'), ('GEEPAS', 'geepas'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('-', ''), ('Vestel-ALBA', 'vestel-alba'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SUNNY', 'sunny'), ('Premier', 'premier'), ('Lifemaxx', 'lifemaxx'), ('Nordmende', 'nordmende'), ('Panasonic', 'panasonic'), ('Skytech', 'skytech'), ('AWOX', 'awox'), ('SHARP', 'sharp'), ('WOON', 'woon'), ('Acer', 'acer'), ('Vestel-Regal', 'vestel-regal'), ('NEXT', 'next'), ('Profilo', 'profilo'), ('SEG', 'seg'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('AXEN', 'axen'), ('Hi-Level', 'hi-level'), ('SAMSUNG', 'samsung'), ('REGAL', 'regal'), ('Navitech', 'navitech'), ('RONAX', 'ronax'), ('ROWELL', 'rowell'), ('PHILIPS', 'philips'), ('Homstar', 'homstar'), ('SUNNY-AXEN', 'sunny-axen')], max_length=100, null=True),
        ),
    ]
