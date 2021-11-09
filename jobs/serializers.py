from rest_framework import serializers
from jobs.models import JobsTime


class HowRead(serializers.ModelSerializer):
    class Meta:
        model = JobsTime
        fields = '__all__'
