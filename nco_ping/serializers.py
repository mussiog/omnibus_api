from rest_framework import serializers
from .models import Nco_ping

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
