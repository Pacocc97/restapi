# Generated by Django 5.0.6 on 2024-05-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PokeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='updated_at',
        ),
    ]