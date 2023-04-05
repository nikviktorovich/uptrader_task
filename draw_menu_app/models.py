from django.db import models
from django.core import validators


# Create your models here.

class Menu(models.Model):
    """Menu model

    Attributes:
        name: Menu name which may be used in url
        readable_name: Name that will be shown to user
        parent: Parent menu (may be None)
    """
    name = models.CharField(max_length=255, unique=True, validators=[
        validators.RegexValidator(
            regex=r'[a-z0-9_-]+',
            message='name may only contain a-z, 0-9, _ and -',
        )
    ])
    readable_name = models.TextField()
    parent = models.ForeignKey(
        'Menu',
        related_name='submenus',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
