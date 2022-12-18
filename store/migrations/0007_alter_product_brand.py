# Generated by Django 4.1.1 on 2022-10-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('ONVO', 'onvo'), ('BEKO', 'beko'), ('CVS', 'cvs'), ('Skytech', 'skytech'), ('SUNNY', 'sunny'), ('VESTEL', 'vestel'), ('Dreamstar', 'dreamstar'), ('AUO', 'auo'), ('TCL', 'tcl'), ('Arçelik-Beko-Grundig', 'arcelik-beko-grundig'), ('Dijitsu', 'dijitsu'), ('GRUNDIG', 'grundig'), ('GEEPAS', 'geepas'), ('SANYO', 'sanyo'), ('SAMSUNG', 'samsung'), ('ALTUS', 'altus'), ('ARÇELİK', 'arcelik'), ('Botech', 'botech'), ('TELENOVA', 'telenova'), ('', ''), ('LG', 'lg'), ('ROWELL', 'rowell'), ('PHILIPS', 'philips'), ('TECHNOBOX', 'technobox'), ('AWOX', 'awox'), ('NEXT', 'next'), ('Next', 'next'), ('Profilo', 'profilo')], max_length=50, null=True),
        ),
    ]
