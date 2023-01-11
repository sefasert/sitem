# Generated by Django 4.1.3 on 2023-01-10 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_alter_product_brand_alter_product_durum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='webp',
            field=models.ImageField(blank=True, null=True, upload_to='webp/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('NEXT', 'next'), ('PHILIPS', 'philips'), ('-', ''), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Osawa', 'osawa'), ('AWOX', 'awox'), ('Lifemaxx', 'lifemaxx'), ('SUNNY-AXEN', 'sunny-axen'), ('YUMATU', 'yumatu'), ('Dijitsu', 'dijitsu'), ('Premier', 'premier'), ('Hisense', 'hisense'), ('ONVO', 'onvo'), ('Homstar', 'homstar'), ('Navitech', 'navitech'), ('SONY', 'sony'), ('Botech', 'botech'), ('SAMSUNG', 'samsung'), ('GEEPAS', 'geepas'), ('Dreamstar', 'dreamstar'), ('Vestel-Toshiba', 'vestel-toshiba'), ('Profilo', 'profilo'), ('CVS', 'cvs'), ('SUNNY', 'sunny'), ('AXEN', 'axen'), ('Skytech', 'skytech'), ('Next', 'next'), ('Nordmende', 'nordmende'), ('LG', 'lg'), ('ROWELL', 'rowell'), ('Panasonic', 'panasonic'), ('SANYO', 'sanyo')], max_length=50, null=True),
        ),
    ]
