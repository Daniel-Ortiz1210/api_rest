# Generated by Django 4.0.6 on 2022-08-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('imc', models.FloatField()),
                ('geb', models.FloatField()),
                ('eta', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
