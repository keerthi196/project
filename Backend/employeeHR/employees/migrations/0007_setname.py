# Generated by Django 3.0.5 on 2020-06-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20200629_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='setname',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
    ]
