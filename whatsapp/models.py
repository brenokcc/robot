from django.db import models

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

    def __str__(self):
        return '{} {}'.format(self.user, self.text)

class IncomeMessage(Message):
    pass

class OutcomeMessage(Message):
    pass
