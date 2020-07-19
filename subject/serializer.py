from subject.models import SubjectModel, Authors
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('name')

class SubjectSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = SubjectModel
        fields = '__all__'

    def get_author(self, obj):
        if obj.author:
            return dict(obj.author)

    def create(self, obj):
        name = obj.get('name')
        genre = obj.get('genre')
        author = obj.get('author')
        subject = SubjectModel(name=name,genre=genre,author=author)
        subject.save()
        
