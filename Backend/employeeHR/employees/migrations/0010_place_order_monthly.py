# Generated by Django 3.0.5 on 2020-07-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_userdaycart_usermonthlycart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place_order_Monthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicetype', models.TextField()),
                ('shopname', models.TextField()),
                ('customername', models.TextField()),
                ('productname', models.TextField()),
                ('price', models.TextField()),
                ('brand', models.TextField()),
                ('quantity', models.TextField()),
            ],
        ),
    ]
