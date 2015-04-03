# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import topnotchdev.files_widget.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_remove_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=topnotchdev.files_widget.fields.ImagesField(null=True),
            preserve_default=True,
        ),
    ]
