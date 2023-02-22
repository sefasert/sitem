# Generated by Django 4.1.3 on 2023-02-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0063_product_ekran_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SUNNY-AXEN', 'sunny-axen'), ('Vestel-SEG', 'vestel-seg'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('SUNNY', 'sunny'), ('DARFON', 'darfon'), ('PHILIPS', 'philips'), ('Homstar', 'homstar'), ('ONVO', 'onvo'), ('Panasonic', 'panasonic'), ('REGAL', 'regal'), ('SANYO', 'sanyo'), ('Hi-Level', 'hi-level'), ('Hisense', 'hisense'), ('ROWELL', 'rowell'), ('Nordmende', 'nordmende'), ('INNOLUX', 'innolux'), ('SAMSUNG', 'samsung'), ('CHIMEI', 'chimei'), ('Vestel-ALBA', 'vestel-alba'), ('NEXT', 'next'), ('AUO', 'auo'), ('SHARP', 'sharp'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('GEEPAS', 'geepas'), ('Lifemaxx', 'lifemaxx'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Vestel-Regal', 'vestel-regal'), ('YUMATU', 'yumatu'), ('AWOX', 'awox'), ('Navitech', 'navitech'), ('Vestel', 'vestel'), ('Profilo', 'profilo'), ('LG', 'lg'), ('Osawa', 'osawa'), ('Premier', 'premier'), ('Dreamstar', 'dreamstar'), ('Dijitsu', 'dijitsu'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Next', 'next'), ('SONY', 'sony'), ('SEG', 'seg'), ('Acer', 'acer'), ('RONAX-TELENOVA', 'ronax-telenova'), ('AXEN', 'axen'), ('BOE', 'boe'), ('-', ''), ('WOON', 'woon'), ('Skytech', 'skytech')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LCD', 'lcd'), ('LED', 'led'), ('Plazma', 'plazma'), ('LED-LCD', 'led-lcd')], max_length=10, null=True),
        ),
    ]
