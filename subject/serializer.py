from subject.models import SubjectModel
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'
