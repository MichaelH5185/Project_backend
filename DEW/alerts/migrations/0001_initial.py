# Generated by Django 5.1.7 on 2025-04-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zipcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znum', models.IntegerField(max_length=5)),
                ('wcode', models.CharField(max_length=100)),
            ],
        ),
    ]
