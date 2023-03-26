from django.db import models

from main.managers import MessageManager


class User(models.Model):
    """
    mock user model
    """
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    channels = models.ManyToManyField("Channel", blank=True, related_name='subscribers')
    subscribe = models.ManyToManyField("MessageCategories", blank=True, related_name='subscribers')

    def __str__(self):
        return self.name


class MessageCategories(models.Model):
    """
    Message categories
    """
    category_choices = [
        ('Sports', 'Sports'),
        ('Finance', 'Finance'),
        ('Movies', 'Movies')
    ]
    name = models.CharField(max_length=25, choices=category_choices, default=category_choices[0][0], unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Message Categories'


class Message(models.Model):
    """
    Messages Model
    """
    category = models.ForeignKey(MessageCategories, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    objects = MessageManager()

    def __str__(self):
        return f"{self.category} - {self.message}"


class Channel(models.Model):
    """
    Notification Channels
    """
    channel_choices = [
        ('SMS', 'SMS'),
        ('E-Mail', 'E-Mail'),
        ('Push Notification', 'Push Notification')
    ]
    name = models.CharField(max_length=25, choices=channel_choices, default=channel_choices[0][0], unique=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    """
    Log model to track notifications
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def message_type(self):
        return self.message.category.name

    @property
    def channel_type(self):
        return self.channel.name

    def __str__(self):
        return f"{self.created_on} -- {self.user} -- {self.channel_type if self.channel else None} -- {self.message_type} -- {self.message.message}"

    def get_log(self):
        return str(self)
