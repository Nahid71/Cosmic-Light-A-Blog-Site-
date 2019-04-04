from django.db import models

# Create your models here.


class Signup(models.Model):
    """Model definition for Singup."""

    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Singup."""

    def __str__(self):
        """Unicode representation of Singup."""
        return self.email
