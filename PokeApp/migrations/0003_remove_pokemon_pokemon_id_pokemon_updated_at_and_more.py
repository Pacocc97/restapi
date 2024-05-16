# Generated by Django 5.0.6 on 2024-05-15 20:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokeApp', '0002_remove_pokemon_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='pokemon_id',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
