# Generated by Django 4.1.3 on 2023-02-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_alter_product_brand_alter_product_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('AWOX', 'awox'), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('SAMSUNG', 'samsung'), ('Vestel-SEG', 'vestel-seg'), ('Hisense', 'hisense'), ('AUO', 'auo'), ('Vestel', 'vestel'), ('Panasonic', 'panasonic'), ('WOON', 'woon'), ('SUNNY', 'sunny'), ('Skytech', 'skytech'), ('ROWELL', 'rowell'), ('SUNNY-AXEN', 'sunny-axen'), ('Next', 'next'), ('AXEN', 'axen'), ('ONVO', 'onvo'), ('RONAX', 'ronax'), ('Hi-Level', 'hi-level'), ('NEXT', 'next'), ('REGAL', 'regal'), ('Profilo', 'profilo'), ('SONY', 'sony'), ('SANYO', 'sanyo'), ('Navitech', 'navitech'), ('Premier', 'premier'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Vestel-ALBA', 'vestel-alba'), ('Nordmende', 'nordmende'), ('Osawa', 'osawa'), ('LG', 'lg'), ('GEEPAS', 'geepas'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('-', ''), ('YUMATU', 'yumatu'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Dreamstar', 'dreamstar'), ('Dijitsu', 'dijitsu'), ('BOE', 'boe'), ('SEG', 'seg'), ('PHILIPS', 'philips'), ('Vestel-Regal', 'vestel-regal'), ('Homstar', 'homstar'), ('SHARP', 'sharp'), ('Lifemaxx', 'lifemaxx'), ('Vestel, Hi-Level', 'vestel,hi-level')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sontarih',
            field=models.DateTimeField(blank=True, default=False, null=True),
        ),
    ]