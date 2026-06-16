from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Watch(models.Model):
    MOVEMENT_CHOICES = [
        ('AUTOMATIC', 'Automatic'),
        ('QUARTZ', 'Quartz'),
        ('MANUAL', 'Manual Winding'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='watches')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    # Technical Specifications
    movement = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    case_size = models.IntegerField(help_text="Size in mm")
    water_resistance = models.CharField(max_length=50, default="50m")
    strap_material = models.CharField(max_length=100)
    
    # Images (Pillow handles this)
    primary_image = models.ImageField(upload_to='watches/')
    secondary_image = models.ImageField(upload_to='watches/', help_text="Shown on hover")
    
    stock = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} - {self.title}"