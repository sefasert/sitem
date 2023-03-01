# Generated by Django 4.1.7 on 2023-02-28 19:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0009_remove_setting_close_time_remove_setting_open_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('brand', models.CharField(blank=True, choices=[('PHILIPS', 'philips'), ('Homstar', 'homstar'), ('Lifemaxx', 'lifemaxx'), ('INNOLUX', 'innolux'), ('Acer', 'acer'), ('Premier', 'premier'), ('AWOX', 'awox'), ('Arçelik-Beko-Grundig-Altus', 'arcelik-beko-grundig-altus'), ('ROWELL', 'rowell'), ('CHIMEI', 'chimei'), ('Vestel-SEG', 'vestel-seg'), ('-', ''), ('Arçelik-Beko-Grundig', 'arçelik-beko-grundig'), ('VESTEL-SEG-REGAL', 'vestel-seg-regal'), ('REGAL', 'regal'), ('Vestel-Techwood-Regal', 'vestel-techwood-regal'), ('Next', 'next'), ('ONVO', 'onvo'), ('Skytech', 'skytech'), ('Dreamstar', 'dreamstar'), ('Vestel-ALBA', 'vestel-alba'), ('Panasonic', 'panasonic'), ('Profilo', 'profilo'), ('Navitech', 'navitech'), ('Nordmende', 'nordmende'), ('MEGMEET', 'megmeet'), ('NEXT', 'next'), ('Vestel', 'vestel'), ('WOON', 'woon'), ('DARFON', 'darfon'), ('YUMATU', 'yumatu'), ('Hisense', 'hisense'), ('Osawa', 'osawa'), ('SUNNY-AXEN', 'sunny-axen'), ('SAMSUNG', 'samsung'), ('AUO', 'auo'), ('LG', 'lg'), ('Vestel-Toshiba-Profilo', 'vestel-toshiba-profilo'), ('Vestel, Hi-Level', 'vestel,hi-level'), ('SUNNY', 'sunny'), ('RONAX-TELENOVA', 'ronax-telenova'), ('Hi-Level', 'hi-level'), ('SHARP', 'sharp'), ('AXEN', 'axen'), ('SANYO', 'sanyo'), ('SEG', 'seg'), ('BOE', 'boe'), ('Dijitsu', 'dijitsu'), ('Vestel-Regal', 'vestel-regal'), ('GEEPAS', 'geepas'), ('SONY', 'sony')], max_length=100)),
                ('durum', models.CharField(blank=True, choices=[('Sıfır', '0'), ('2.EL', '2')], max_length=50)),
                ('yeni', models.CharField(blank=True, choices=[('Yeni', 'yeni')], max_length=10)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='photos/products')),
                ('webp', models.ImageField(blank=True, null=True, upload_to='webp/products')),
                ('images2', models.ImageField(blank=True, null=True, upload_to='photos2/products')),
                ('webp2', models.ImageField(blank=True, null=True, upload_to='webp2/products')),
                ('stock', models.IntegerField()),
                ('ekran', models.CharField(blank=True, choices=[('Plazma', 'plazma'), ('LED-LCD', 'led-lcd'), ('LCD', 'lcd'), ('LED', 'led')], max_length=10)),
                ('tags', models.TextField(blank=True, max_length=1000)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('is_available', models.BooleanField(default=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('sontarih', models.DateTimeField(blank=True, default=False)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(blank=True, default=0)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='Related_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benzerresimlink', models.CharField(blank=True, max_length=200)),
                ('benzerad', models.CharField(max_length=200)),
                ('benzerlink', models.CharField(max_length=200)),
                ('benzerfiyat', models.IntegerField()),
                ('benzerstok', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'related product',
            },
        ),
    ]
