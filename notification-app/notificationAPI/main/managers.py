from django.db import models
from .notifications import *


class MessageManager(models.Manager):
    """
    Custom Message manager for sending notifications
    """
    def create(self, *args, **kwargs):
        message = super(MessageManager, self).create(*args, **kwargs)
        if message.category:
            for dispatcher in NotificationDispatcher.__subclasses__():
                dispatcher().send_notification(message)
        return message
