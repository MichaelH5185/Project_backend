# Generated by Django 5.1.7 on 2025-04-03 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_alter_zipcode_znum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('ends', models.CharField(max_length=50)),
                ('instruct', models.CharField(max_length=400)),
                ('severity', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
                ('ref_url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alerts.zipcode')),
            ],
        ),
    ]
