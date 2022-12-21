# Generated by Django 4.1.3 on 2022-12-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_brand_alter_product_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('SONY', 'sony'), ('ONVO', 'onvo'), ('SAMSUNG', 'samsung'), ('Panasonic', 'panasonic'), ('VESTEL', 'vestel'), ('Botech', 'botech'), ('TCL', 'tcl'), ('TELENOVA', 'telenova'), ('NEXT', 'next'), ('SANYO', 'sanyo'), ('Profilo', 'profilo'), ('Dijitsu', 'dijitsu'), ('-', ''), ('CVS', 'cvs'), ('LG', 'lg'), ('GEEPAS', 'geepas'), ('Dreamstar', 'dreamstar'), ('Premier', 'premier'), ('TECHNOBOX', 'technobox'), ('YUMATU', 'yumatu'), ('Homstar', 'homstar'), ('SUNNY', 'sunny'), ('TOSHIBA', 'toshiba'), ('ROWELL', 'rowell'), ('SUNNY-AXEN', 'sunny-axen'), ('AWOX', 'awox'), ('Skytech', 'skytech'), ('Next', 'next'), ('PHILIPS', 'philips'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('Nordmende', 'nordmende'), ('AXEN', 'axen'), ('Navitech', 'navitech')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('2.EL', '2'), ('Sıfır', '0')], max_length=50, null=True),
        ),
    ]
