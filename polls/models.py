import uuid

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_datetime(datetime):
    if datetime < timezone.now():
        raise ValidationError("Date cannot be in the past")


class Poll(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=250)
    duration = models.DateTimeField(validators=[validate_datetime])
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question



class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
