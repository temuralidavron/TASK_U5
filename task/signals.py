from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification
from task.models import Task


@receiver(post_save,sender=Task)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            to_user=instance.assign_to,
            title=instance.title,
            description=instance.description,

        )
    else:
        Notification.objects.create(
            to_user=instance.assign_to,
            title=instance.title,
            description=instance.description,

        )

