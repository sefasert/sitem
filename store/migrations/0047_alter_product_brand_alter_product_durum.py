# Generated by Django 4.1.3 on 2023-02-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Vestel, Hi-Level', 'vestel,hi-level'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Lifemaxx', 'lifemaxx'), ('Hisense', 'hisense'), ('-', ''), ('AUO', 'auo'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Navitech', 'navitech'), ('Vestel-SEG', 'vestel-seg'), ('PHILIPS', 'philips'), ('Skytech', 'skytech'), ('Hi-Level', 'hi-level'), ('REGAL', 'regal'), ('LG', 'lg'), ('Profilo', 'profilo'), ('Panasonic', 'panasonic'), ('SUNNY', 'sunny'), ('YUMATU', 'yumatu'), ('Next', 'next'), ('Vestel', 'vestel'), ('Dreamstar', 'dreamstar'), ('BOE', 'boe'), ('Dijitsu', 'dijitsu'), ('Nordmende', 'nordmende'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Vestel-Regal', 'vestel-regal'), ('SUNNY-AXEN', 'sunny-axen'), ('Premier', 'premier'), ('RONAX', 'ronax'), ('AWOX', 'awox'), ('GEEPAS', 'geepas'), ('Osawa', 'osawa'), ('Vestel-ALBA', 'vestel-alba'), ('SONY', 'sony'), ('NEXT', 'next'), ('ROWELL', 'rowell'), ('SEG', 'seg'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SAMSUNG', 'samsung'), ('ONVO', 'onvo'), ('Homstar', 'homstar'), ('SHARP', 'sharp'), ('SANYO', 'sanyo'), ('AXEN', 'axen'), ('WOON', 'woon')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50, null=True),
        ),
    ]
