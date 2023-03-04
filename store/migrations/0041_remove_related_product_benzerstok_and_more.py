# Generated by Django 4.1.7 on 2023-03-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='related_product',
            name='benzerstok',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('ONVO', 'onvo'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('Homstar', 'homstar'), ('Vestel-ALBA', 'vestel-alba'), ('AUO', 'auo'), ('Next', 'next'), ('BOE', 'boe'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Lifemaxx', 'lifemaxx'), ('SEG', 'seg'), ('YUMATU', 'yumatu'), ('ROWELL', 'rowell'), ('Dijitsu', 'dijitsu'), ('Nordmende', 'nordmende'), ('Navitech', 'navitech'), ('Dreamstar', 'dreamstar'), ('Panasonic', 'panasonic'), ('Vestel', 'vestel'), ('Profilo', 'profilo'), ('LG', 'lg'), ('Vestel-SEG', 'vestel-seg'), ('SAMSUNG', 'samsung'), ('PHILIPS', 'philips'), ('AWOX', 'awox'), ('SONY', 'sony'), ('REGAL', 'regal'), ('SUNNY-AXEN', 'sunny-axen'), ('SUNNY', 'sunny'), ('WOON', 'woon'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Premier', 'premier'), ('NEXT', 'next'), ('DARFON', 'darfon'), ('RONAX-TELENOVA', 'ronax-telenova'), ('AXEN', 'axen'), ('CHIMEI', 'chimei'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('Acer', 'acer'), ('Hisense', 'hisense'), ('Vestel-Regal', 'vestel-regal'), ('GEEPAS', 'geepas'), ('INNOLUX', 'innolux'), ('Skytech', 'skytech'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('-', ''), ('Osawa', 'osawa'), ('SANYO', 'sanyo'), ('Hi-Level', 'hi-level'), ('SHARP', 'sharp'), ('MEGMEET', 'megmeet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='ekran',
            field=models.CharField(blank=True, choices=[('LED-LCD', 'led-lcd'), ('LCD', 'lcd'), ('LED', 'led'), ('Plazma', 'plazma')], max_length=10),
        ),
    ]