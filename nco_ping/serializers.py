from rest_framework import serializers
from .models import NcoPing

class NcoPingSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField()
    delay = serializers.ReadOnlyField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = NcoPing
        fields = ['id', 'host', 'delay', 'description', 'lastedit']
