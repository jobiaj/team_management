from collections import namedtuple

from django.db import models
from django.core.validators import validate_email


class Teammembers(models.Model):
    ROLE_IDS = namedtuple(
        'ROLE_IDS', ['REGULAR', 'ADMIN'])(*list(range(0, 2)))
    first_name = models.CharField(max_length=254, blank=False, null=False)
    last_name = models.CharField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=64, blank=False, null=False)
    email = models.CharField(max_length=254, blank=False, null=False, validators=[validate_email])
    role = models.PositiveSmallIntegerField(
        choices=[(0, 'REGULAR'), (1, 'ADMIN')],
        default=ROLE_IDS.REGULAR)