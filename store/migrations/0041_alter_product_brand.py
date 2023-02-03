# Generated by Django 4.1.3 on 2023-02-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SONY', 'sony'), ('ONVO', 'onvo'), ('Premier', 'premier'), ('Skytech', 'skytech'), ('REGAL', 'regal'), ('Lifemaxx', 'lifemaxx'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Nordmende', 'nordmende'), ('SAMSUNG', 'samsung'), ('SUNNY', 'sunny'), ('SHARP', 'sharp'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('PHILIPS', 'philips'), ('GEEPAS', 'geepas'), ('RONAX', 'ronax'), ('NEXT', 'next'), ('Homstar', 'homstar'), ('AUO', 'auo'), ('Vestel', 'vestel'), ('ROWELL', 'rowell'), ('YUMATU', 'yumatu'), ('AXEN', 'axen'), ('SANYO', 'sanyo'), ('Osawa', 'osawa'), ('Vestel-SEG', 'vestel-seg'), ('Hisense', 'hisense'), ('Next', 'next'), ('BOE', 'boe'), ('Navitech', 'navitech'), ('-', ''), ('Vestel-Regal', 'vestel-regal'), ('WOON', 'woon'), ('Panasonic', 'panasonic'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Dijitsu', 'dijitsu'), ('SUNNY-AXEN', 'sunny-axen'), ('AWOX', 'awox'), ('LG', 'lg'), ('SEG', 'seg'), ('Vestel-ALBA', 'vestel-alba'), ('Hi-Level', 'hi-level'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Profilo', 'profilo'), ('Dreamstar', 'dreamstar')], max_length=100, null=True),
        ),
    ]