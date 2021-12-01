import uuid

from django.db import models
from django.contrib.auth.models import User


class Counter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='counters'
    )
    current_value = models.IntegerField()

    def __str__(self):
        return self.name


class History(models.Model):
    class UserType(models.IntegerChoices):
        USER = 0, 'User'
        OPERATOR = 1, 'Operator'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    period = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(
        choices=UserType.choices, null=True, blank=True, default=None
    )
    value = models.IntegerField()
    consumption = models.IntegerField()
    counter = models.ForeignKey(Counter, on_delete=models.CASCADE)




