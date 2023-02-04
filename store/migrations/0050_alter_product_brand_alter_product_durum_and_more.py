# Generated by Django 4.1.3 on 2023-02-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_product_images2_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SEG', 'seg'), ('Vestel-Regal', 'vestel-regal'), ('Homstar', 'homstar'), ('YUMATU', 'yumatu'), ('Hi-Level', 'hi-level'), ('Hisense', 'hisense'), ('BOE', 'boe'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Skytech', 'skytech'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('GEEPAS', 'geepas'), ('NEXT', 'next'), ('Lifemaxx', 'lifemaxx'), ('AUO', 'auo'), ('WOON', 'woon'), ('SONY', 'sony'), ('RONAX', 'ronax'), ('Vestel-SEG', 'vestel-seg'), ('Panasonic', 'panasonic'), ('LG', 'lg'), ('Osawa', 'osawa'), ('ROWELL', 'rowell'), ('Navitech', 'navitech'), ('AXEN', 'axen'), ('SAMSUNG', 'samsung'), ('AWOX', 'awox'), ('Vestel', 'vestel'), ('REGAL', 'regal'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SUNNY-AXEN', 'sunny-axen'), ('SANYO', 'sanyo'), ('-', ''), ('Vestel, Hi-Level', 'vestel,hi-level'), ('Dreamstar', 'dreamstar'), ('Nordmende', 'nordmende'), ('ONVO', 'onvo'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SUNNY', 'sunny'), ('Dijitsu', 'dijitsu'), ('PHILIPS', 'philips'), ('Next', 'next'), ('Premier', 'premier'), ('SHARP', 'sharp'), ('Profilo', 'profilo'), ('Vestel-ALBA', 'vestel-alba')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='images2',
            field=models.ImageField(blank=True, null=True, upload_to='photos2/products'),
        ),
    ]