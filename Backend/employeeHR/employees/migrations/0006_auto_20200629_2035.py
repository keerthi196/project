# Generated by Django 3.0.5 on 2020-06-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.TextField()),
                ('category', models.TextField()),
                ('productname', models.TextField()),
                ('price', models.TextField()),
                ('brand', models.TextField()),
                ('quantity', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]