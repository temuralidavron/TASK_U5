from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'title',
            'description',
            'is_read',
            'to_user',
            'created_at',
        ]


class EmptySerializer(serializers.Serializer):
    pass