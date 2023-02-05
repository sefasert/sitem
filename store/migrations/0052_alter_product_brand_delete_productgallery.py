# Generated by Django 4.1.3 on 2023-02-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_product_webp2_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SANYO', 'sanyo'), ('SAMSUNG', 'samsung'), ('SONY', 'sony'), ('Osawa', 'osawa'), ('Vestel-ALBA', 'vestel-alba'), ('SHARP', 'sharp'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('SUNNY-AXEN', 'sunny-axen'), ('YUMATU', 'yumatu'), ('Dijitsu', 'dijitsu'), ('-', ''), ('Vestel-SEG', 'vestel-seg'), ('Next', 'next'), ('SUNNY', 'sunny'), ('Lifemaxx', 'lifemaxx'), ('RONAX', 'ronax'), ('Vestel-Regal', 'vestel-regal'), ('Hisense', 'hisense'), ('Nordmende', 'nordmende'), ('LG', 'lg'), ('ROWELL', 'rowell'), ('Profilo', 'profilo'), ('BOE', 'boe'), ('Panasonic', 'panasonic'), ('SEG', 'seg'), ('ONVO', 'onvo'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('AXEN', 'axen'), ('REGAL', 'regal'), ('WOON', 'woon'), ('AWOX', 'awox'), ('GEEPAS', 'geepas'), ('Skytech', 'skytech'), ('Homstar', 'homstar'), ('Navitech', 'navitech'), ('PHILIPS', 'philips'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Premier', 'premier'), ('AUO', 'auo'), ('NEXT', 'next'), ('Hi-Level', 'hi-level'), ('Vestel', 'vestel'), ('Dreamstar', 'dreamstar')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='ProductGallery',
        ),
    ]