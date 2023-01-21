# Generated by Django 4.1.3 on 2023-01-20 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_remove_productgallery_benzerad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('ONVO', 'onvo'), ('BOE', 'boe'), ('Next', 'next'), ('Dijitsu', 'dijitsu'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('SUNNY-AXEN', 'sunny-axen'), ('Lifemaxx', 'lifemaxx'), ('Dreamstar', 'dreamstar'), ('Botech', 'botech'), ('SAMSUNG', 'samsung'), ('LG', 'lg'), ('Hisense', 'hisense'), ('GEEPAS', 'geepas'), ('PHILIPS', 'philips'), ('ROWELL', 'rowell'), ('YUMATU', 'yumatu'), ('Panasonic', 'panasonic'), ('SONY', 'sony'), ('Vestel-Toshiba', 'vestel-toshiba'), ('RONAX', 'ronax'), ('NEXT', 'next'), ('ALBA', 'alba'), ('SEG', 'seg'), ('-', ''), ('Navitech', 'navitech'), ('Osawa', 'osawa'), ('AWOX', 'awox'), ('SANYO', 'sanyo'), ('Skytech', 'skytech'), ('Nordmende', 'nordmende'), ('SUNNY', 'sunny'), ('CVS', 'cvs'), ('AXEN', 'axen'), ('Premier', 'premier'), ('Hi-Level', 'hi-level'), ('WOON', 'woon'), ('Profilo', 'profilo'), ('Homstar', 'homstar')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Related_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benzerad', models.CharField(max_length=200)),
                ('benzerlink', models.CharField(max_length=200)),
                ('benzerfiyat', models.IntegerField()),
                ('benzerstok', models.IntegerField()),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'related product',
            },
        ),
    ]
