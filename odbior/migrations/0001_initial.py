# Generated by Django 4.0.5 on 2022-06-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zgloszenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst', models.CharField(max_length=200)),
                ('nazwa_autora', models.CharField(max_length=200)),
                ('data_publikacji', models.DateTimeField(verbose_name='data publikacji')),
            ],
        ),
    ]
