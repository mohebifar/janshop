# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', models.FilePathField(null=True, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Product Detail',
                'verbose_name_plural': 'Product Details',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('amount', models.FloatField()),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('long_name', models.CharField(max_length=255, verbose_name='Long Name', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('image', models.ImageField(upload_to=b'static/media', null=True, verbose_name='Product Main Image')),
                ('images', filebrowser.fields.FileBrowseField(max_length=500, verbose_name='Images')),
                ('categories', models.ManyToManyField(to='commerce.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('type', models.CharField(max_length=15, verbose_name='Field Type', choices=[(b'number', b'Number'), (b'boolean', b'Boolean'), (b'text', b'Text')])),
            ],
            options={
                'verbose_name': 'Product Property',
                'verbose_name_plural': 'Product Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('properties', models.ManyToManyField(to='commerce.Property', verbose_name='Properties')),
            ],
            options={
                'verbose_name': 'Product Structure',
                'verbose_name_plural': 'Product Structures',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='prices',
            name='product',
            field=models.ForeignKey(to='commerce.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='product',
            field=models.ForeignKey(verbose_name='Product', to='commerce.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='property',
            field=models.ForeignKey(verbose_name='Product Property', to='commerce.Property'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='structures',
            field=models.ManyToManyField(to='commerce.Structure', verbose_name='Product Structures'),
            preserve_default=True,
        ),
    ]
