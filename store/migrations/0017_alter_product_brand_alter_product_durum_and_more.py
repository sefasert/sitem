# Generated by Django 4.1.7 on 2023-02-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Lifemaxx', 'lifemaxx'), ('SHARP', 'sharp'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SAMSUNG', 'samsung'), ('Dreamstar', 'dreamstar'), ('Vestel-ALBA', 'vestel-alba'), ('Next', 'next'), ('MEGMEET', 'megmeet'), ('WOON', 'woon'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Osawa', 'osawa'), ('GEEPAS', 'geepas'), ('AUO', 'auo'), ('-', ''), ('NEXT', 'next'), ('SEG', 'seg'), ('SUNNY', 'sunny'), ('ONVO', 'onvo'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Panasonic', 'panasonic'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Vestel', 'vestel'), ('PHILIPS', 'philips'), ('SONY', 'sony'), ('Dijitsu', 'dijitsu'), ('DARFON', 'darfon'), ('AWOX', 'awox'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Vestel-Regal', 'vestel-regal'), ('Vestel-SEG', 'vestel-seg'), ('Hi-Level', 'hi-level'), ('INNOLUX', 'innolux'), ('AXEN', 'axen'), ('Acer', 'acer'), ('BOE', 'boe'), ('SANYO', 'sanyo'), ('Hisense', 'hisense'), ('CHIMEI', 'chimei'), ('Profilo', 'profilo'), ('REGAL', 'regal'), ('RONAX-TELENOVA', 'ronax-telenova'), ('YUMATU', 'yumatu'), ('Skytech', 'skytech'), ('Navitech', 'navitech'), ('Homstar', 'homstar'), ('ROWELL', 'rowell'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SUNNY-AXEN', 'sunny-axen'), ('Premier', 'premier'), ('Nordmende', 'nordmende'), ('LG', 'lg')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED', 'led'), ('Plazma', 'plazma'), ('LCD', 'lcd'), ('LED-LCD', 'led-lcd')], max_length=10),
        ),
    ]
