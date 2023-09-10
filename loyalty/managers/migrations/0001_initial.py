# Generated by Django 4.1.10 on 2023-08-27 00:09

from django.db import migrations, models
import djongo.models.fields
import shops.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('shops', djongo.models.fields.EmbeddedField(model_container=shops.models.Shop)),
            ],
        ),
    ]
