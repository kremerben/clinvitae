# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenomicVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nucleotide_change', models.TextField(blank=True)),
                ('protein_change', models.TextField(blank=True)),
                ('other_mappings', models.TextField(blank=True)),
                ('alias', models.TextField(blank=True)),
                ('transcripts', models.TextField(blank=True)),
                ('region', models.TextField(blank=True)),
                ('reported_classification', models.TextField(blank=True)),
                ('inferred_classification', models.TextField(blank=True)),
                ('source', models.TextField(blank=True)),
                ('last_evaluated', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('submitter_comment', models.TextField(blank=True)),
                ('assembly', models.TextField(blank=True)),
                ('chr', models.TextField(blank=True)),
                ('genomic_start', models.TextField(blank=True)),
                ('genomic_stop', models.TextField(blank=True)),
                ('ref', models.TextField(blank=True)),
                ('alt', models.TextField(blank=True)),
                ('accession', models.TextField(blank=True)),
                ('reported_ref', models.TextField(blank=True)),
                ('reported_alt', models.TextField(blank=True)),
                ('gene', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='genomic_variants.Gene')),
            ],
        ),
    ]
