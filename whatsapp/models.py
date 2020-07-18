from django.db import models
from uuid import uuid1

class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserService(models.Model):
    user = models.CharField(max_length=50)
    service = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.user, self.service)


class Message(models.Model):
    user = models.CharField(max_length=50)
    text = models.TextField()
    delivered = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)
    uuid = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.user, self.text)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid1().hex
        super().save(*args, **kwargs)

class IncomeMessage(Message):
    pass

class OutcomeMessage(Message):
    pass
