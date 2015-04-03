# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='commerce.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(upload_to=b'', null=True, verbose_name='Image'),
            preserve_default=True,
        ),
    ]
