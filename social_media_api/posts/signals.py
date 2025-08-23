from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, Comment
from notifications.models import Notification


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.user:  # don’t notify self-like
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.user,
            verb="liked your post",
            target=instance.post
        )


@receiver(post_delete, sender=Like)
def delete_like_notification(sender, instance, **kwargs):
    # Optional: remove notification when like is undone
    Notification.objects.filter(
        recipient=instance.post.author,
        actor=instance.user,
        verb="liked your post",
        target_object_id=instance.post.id
    ).delete()

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.author,
            verb="commented on your post",
            target=instance.post
        )
