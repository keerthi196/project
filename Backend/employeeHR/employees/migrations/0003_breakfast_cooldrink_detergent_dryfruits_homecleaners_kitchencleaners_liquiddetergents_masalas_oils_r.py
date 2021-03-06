# Generated by Django 3.0.5 on 2020-05-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_deliveryboyregister_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='breakfast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cooldrink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='detergent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='dryfruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='homecleaners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='kitchencleaners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='liquiddetergents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='masalas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='oils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='rice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='snacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='syrups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
