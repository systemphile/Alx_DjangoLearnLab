from django.urls import path
from .views import NotificationListView, UnreadNotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='all-notifications'),
    path('unread/', UnreadNotificationListView.as_view(), name='unread-notifications'),
]
