# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 13:49
from __future__ import unicode_literals

import activflow.tests.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20170624_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooMoreLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plughmore', models.CharField(max_length=200, validators=[activflow.tests.validators.validate_initial_cap], verbose_name='Plughmore')),
                ('thudmore', models.CharField(choices=[('GR', 'Grault'), ('GA', 'Garply')], max_length=30, verbose_name='Thudmore')),
                ('foo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='morelines', to='tests.Foo')),
            ],
        ),
        migrations.AlterField(
            model_name='foolineitem',
            name='foo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='tests.Foo'),
        ),
    ]