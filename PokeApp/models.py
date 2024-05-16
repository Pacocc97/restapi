import uuid
from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pokemon_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    types = models.JSONField()  # Almacena tipos como un array en JSON
    abilities = models.JSONField()  # Almacena habilidades como un array en JSON
    base_stats = models.JSONField()
    height = models.FloatField()
    weight = models.FloatField()
    sprite_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  