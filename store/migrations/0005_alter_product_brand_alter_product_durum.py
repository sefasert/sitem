# Generated by Django 4.1.1 on 2022-10-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('NEXT', 'next'), ('BEKO', 'beko'), ('TELENOVA', 'telenova'), ('VESTEL', 'vestel'), ('Dijitsu', 'dijitsu'), ('TCL', 'tcl'), ('GRUNDIG', 'grundig'), ('AUO', 'auo'), ('ARÇELİK', 'arcelik'), ('LG', 'lg'), ('AWOX', 'awox'), ('PHILIPS', 'philips'), ('Arçelik-Beko-Grundig', 'arcelik-beko-grundig'), ('Profilo', 'profilo'), ('CVS', 'cvs'), ('TECHNOBOX', 'technobox'), ('Dreamstar', 'dreamstar'), ('SANYO', 'sanyo'), ('Botech', 'botech'), ('SUNNY', 'sunny'), ('SAMSUNG', 'samsung')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='durum',
            field=models.CharField(blank=True, choices=[('0', '0'), ('2.EL', '2')], max_length=50, null=True),
        ),
    ]
