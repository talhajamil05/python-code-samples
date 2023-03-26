from django.apps import apps


class NotificationDispatcher:
    """
    Base Notification Dispatcher
    """
    def send_notification(self, message, channel):
        try:
            channel_obj = apps.get_model('main.Channel').objects.get(name=channel)

            for user in channel_obj.subscribers.all() & message.category.subscribers.all():
                apps.get_model('main.Log').objects.create(
                    user=user,
                    message=message,
                    channel=channel_obj
                )
        except apps.get_model('main.Channel').DoesNotExist:
            return False


class SMSNotificationDispatcher(NotificationDispatcher):
    """
    Custom notification class for sending SMS notifications
    """
    def send_notification(self, message, channel=None):
        super().send_notification(message, 'SMS')


class PushNotificationDispatcher(NotificationDispatcher):
    """
    Custom notification class for sending PUSH notifications
    """
    def send_notification(self, message, channel=None):
        super().send_notification(message, 'Push Notification')


class EmailNotificationDispatcher(NotificationDispatcher):
    """
    Custom notification class for sending email notifications
    """
    def send_notification(self, message, channel=None):
        super().send_notification(message, 'E-Mail')
