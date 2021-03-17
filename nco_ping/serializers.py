from rest_framework import serializers
from .models import Nco_ping

class NcoPingSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='poster.username')
    delay = serializers.ReadOnlyField(source='poster.id')
    description = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'host', 'delay', 'description', 'lastedit']
