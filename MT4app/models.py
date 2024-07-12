from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        ('1', 'Poor'),
        ('2', 'Fair'),
        ('3', 'Good'),
        ('4', 'Very Good'),
        ('5', 'Excellent'),
    )

    service = models.ForeignKey(Service, related_name='reviews', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='3')

    def __str__(self):
        return f'Review by {self.customer.username} on {self.service.name}'
