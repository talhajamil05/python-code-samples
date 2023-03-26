from rest_framework import serializers
from .models import Log, Message


class LogSerializer(serializers.ModelSerializer):
    """
    Log serializer
    """
    class Meta:
        model = Log
        fields = "__all__"
        depth = 1


class LogStringSerializer(serializers.ModelSerializer):
    """
    Log String representation serializer
    """
    log = serializers.CharField(source='get_log')

    class Meta:
        model = Log
        fields = ['log']


class MessageSerializer(serializers.ModelSerializer):
    """
    Message data serializer
    """
    class Meta:
        model = Message
        fields = '__all__'
