from rest_framework import serializers
from libapp.models import bdb

class serialb(serializers.ModelSerializer):
    class Meta:
        model = bdb
        fields = (
            'bid',
            'bname',
            'aname',
            'description',
            'price',
        )