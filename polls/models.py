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

    def get_total_seconds(self):
        return (self.duration - self.pub_date).total_seconds()

    def is_expired(self):
        if self.duration >= timezone.now():
            return False
        return True


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def get_percentage(self):
        poll = Poll.objects.get(choice=self.pk)
        choices = Choice.objects.filter(poll=poll.pk)
        
        total_count = 0
        for choice in choices:
            total_count = total_count + choice.votes

        votes = self.votes
        if total_count == 0:
            percentage = 0
        else:
            percentage = votes * 100 / total_count
        return percentage
