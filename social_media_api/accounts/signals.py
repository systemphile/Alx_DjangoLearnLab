from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.conf import settings
from notifications.models import Notification

User = settings.AUTH_USER_MODEL


@receiver(m2m_changed, sender=settings.AUTH_USER_MODEL.following.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    # instance = user performing follow
    if action == "post_add":
        for user_id in pk_set:
            if instance.id != user_id:
                Notification.objects.create(
                    recipient_id=user_id,
                    actor=instance,
                    verb="started following you"
                )
    elif action == "post_remove":
        for user_id in pk_set:
            Notification.objects.filter(
                recipient_id=user_id,
                actor=instance,
                verb="started following you"
            ).delete()