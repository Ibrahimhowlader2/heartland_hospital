from django.db import models
from django.core.validators import RegexValidator

class ContactUs(models.Model):
    phone_validator = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}$',
        message="Enter a valid phone number (e.g., +123456789)."
    )
    
    name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_validator], max_length=16, blank=True)
    problem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Contact Us"
