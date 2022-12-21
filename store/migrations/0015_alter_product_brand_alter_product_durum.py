# Generated by Django 4.1.3 on 2022-12-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('TECHNOBOX', 'technobox'), ('SUNNY-AXEN', 'sunny-axen'), ('Profilo', 'profilo'), ('Dreamstar', 'dreamstar'), ('SUNNY', 'sunny'), ('-', ''), ('YUMATU', 'yumatu'), ('NEXT', 'next'), ('LG', 'lg'), ('SAMSUNG', 'samsung'), ('Homstar', 'homstar'), ('Premier', 'premier'), ('Navitech', 'navitech'), ('Nordmende', 'nordmende'), ('Next', 'next'), ('Panasonic', 'panasonic'), ('TCL', 'tcl'), ('AXEN', 'axen'), ('CVS', 'cvs'), ('TOSHIBA', 'toshiba'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('ONVO', 'onvo'), ('ROWELL', 'rowell'), ('SANYO', 'sanyo'), ('AWOX', 'awox'), ('GEEPAS', 'geepas'), ('Dijitsu', 'dijitsu'), ('TELENOVA', 'telenova'), ('Botech', 'botech'), ('Skytech', 'skytech'), ('PHILIPS', 'philips'), ('SONY', 'sony'), ('VESTEL', 'vestel')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50, null=True),
        ),
    ]
