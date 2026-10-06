from django.db import models

class Service(models.Model):
    """Services offered by SEYNARA"""
    PILLAR_CHOICES = [
        ('elegance', 'Élégance'),
        ('emotion', 'Émotion'),
        ('design', 'Design'),
        ('detail', 'Détail'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    pillar = models.CharField(max_length=20, choices=PILLAR_CHOICES)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Event(models.Model):
    """Portfolio of SEYNARA events"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    date = models.DateField()
    location = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Événement'
        verbose_name_plural = 'Événements'

    def __str__(self):
        return self.title


class Contact(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Demande de contact'
        verbose_name_plural = 'Demandes de contact'

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y')}"
