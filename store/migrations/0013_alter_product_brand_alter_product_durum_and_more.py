# Generated by Django 4.1.7 on 2023-02-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_brand_alter_product_ekran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Dreamstar', 'dreamstar'), ('INNOLUX', 'innolux'), ('RONAX-TELENOVA', 'ronax-telenova'), ('SUNNY-AXEN', 'sunny-axen'), ('Nordmende', 'nordmende'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Next', 'next'), ('BOE', 'boe'), ('ONVO', 'onvo'), ('AXEN', 'axen'), ('SHARP', 'sharp'), ('WOON', 'woon'), ('Vestel-SEG', 'vestel-seg'), ('AWOX', 'awox'), ('Lifemaxx', 'lifemaxx'), ('Hi-Level', 'hi-level'), ('SONY', 'sony'), ('Homstar', 'homstar'), ('CHIMEI', 'chimei'), ('GEEPAS', 'geepas'), ('Vestel', 'vestel'), ('AUO', 'auo'), ('Profilo', 'profilo'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Navitech', 'navitech'), ('Osawa', 'osawa'), ('Vestel-ALBA', 'vestel-alba'), ('SEG', 'seg'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('ROWELL', 'rowell'), ('Panasonic', 'panasonic'), ('Hisense', 'hisense'), ('Acer', 'acer'), ('YUMATU', 'yumatu'), ('-', ''), ('PHILIPS', 'philips'), ('NEXT', 'next'), ('Dijitsu', 'dijitsu'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('REGAL', 'regal'), ('Skytech', 'skytech'), ('SUNNY', 'sunny'), ('LG', 'lg'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('SAMSUNG', 'samsung'), ('MEGMEET', 'megmeet'), ('Premier', 'premier'), ('DARFON', 'darfon'), ('SANYO', 'sanyo'), ('Vestel-Regal', 'vestel-regal')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED', 'led'), ('LCD', 'lcd'), ('Plazma', 'plazma'), ('LED-LCD', 'led-lcd')], max_length=10),
        ),
    ]
