# Generated by Django 4.1.7 on 2023-02-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('Lifemaxx', 'lifemaxx'), ('SUNNY-AXEN', 'sunny-axen'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('SUNNY', 'sunny'), ('Vestel-SEG', 'vestel-seg'), ('BOE', 'boe'), ('GEEPAS', 'geepas'), ('DARFON', 'darfon'), ('Acer', 'acer'), ('Nordmende', 'nordmende'), ('Profilo', 'profilo'), ('Next', 'next'), ('SANYO', 'sanyo'), ('Dijitsu', 'dijitsu'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Hi-Level', 'hi-level'), ('PHILIPS', 'philips'), ('Vestel-Regal', 'vestel-regal'), ('SAMSUNG', 'samsung'), ('SEG', 'seg'), ('WOON', 'woon'), ('Panasonic', 'panasonic'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Hisense', 'hisense'), ('MEGMEET', 'megmeet'), ('Osawa', 'osawa'), ('Premier', 'premier'), ('LG', 'lg'), ('AXEN', 'axen'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Skytech', 'skytech'), ('-', ''), ('INNOLUX', 'innolux'), ('NEXT', 'next'), ('SONY', 'sony'), ('AWOX', 'awox'), ('SHARP', 'sharp'), ('CHIMEI', 'chimei'), ('Vestel', 'vestel'), ('Navitech', 'navitech'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Dreamstar', 'dreamstar'), ('ROWELL', 'rowell'), ('YUMATU', 'yumatu'), ('ONVO', 'onvo'), ('Vestel-ALBA', 'vestel-alba'), ('REGAL', 'regal'), ('AUO', 'auo'), ('Homstar', 'homstar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LCD', 'lcd'), ('LED-LCD', 'led-lcd'), ('Plazma', 'plazma'), ('LED', 'led')], max_length=10),
        ),
    ]
