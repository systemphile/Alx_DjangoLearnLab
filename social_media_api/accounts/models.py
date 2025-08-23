from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    # Users that follow this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',  # allows reverse lookup
        blank=True
    )

    def follow(self, user):
        """Follow another user"""
        if user != self:  # prevent self-follow
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        self.following.remove(user)

    def is_following(self, user):
        """Check if current user follows another"""
        return self.following.filter(id=user.id).exists()

    def is_followed_by(self, user):
        """Check if current user is followed by another"""
        return self.followers.filter(id=user.id).exists()
