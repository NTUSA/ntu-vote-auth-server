# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-25 18:19
from __future__ import unicode_literals

from django.db import migrations

from core import meta


def fowards_func(apps, schema_editor):
    Entry = apps.get_model('core', 'Entry')
    db_alias = schema_editor.connection.alias
    Entry.objects.using(db_alias).bulk_create([
        Entry(dpt_code=key, name=meta.DPTCODE_NAME[key]) for key in meta.DPTCODE_NAME
    ])


def reverse_func(apps, schema_editor):
    Entry = apps.get_model('core', 'Entry')
    db_alias = schema_editor.connection.alias
    for entry in Entry.objects.using(db_alias).all():
        if entry.dpt_code in meta.DPTCODE_NAME:
            entry.delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial')
    ]

    operations = [
        migrations.RunPython(fowards_func, reverse_func),
    ]
