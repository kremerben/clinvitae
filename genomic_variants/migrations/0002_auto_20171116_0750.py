# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genomic_variants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genomicvariant',
            name='last_evaluated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genomicvariant',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
