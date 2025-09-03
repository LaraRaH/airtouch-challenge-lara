from django.db import models
from django.contrib.auth.models import User


class NutritionalInformation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nutritionalinformation'  # nombre exacto de tu tabla
        managed = False  # ya existe en MySQL

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Product(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    nutritional_values = models.JSONField(
        blank=True, null=True)  # 👈 columna JSON
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        managed = False  # como la tabla ya existe en tu DB

    def __str__(self):
        return self.name
