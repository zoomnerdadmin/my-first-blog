from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    #author = serializers.ForeignKey('auth.User')
    author = serializers.RelatedField(source='auth.User', read_only=True)

    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    created_date = serializers.DateTimeField()
    published_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self,instance, Validated_data):
        
        instance.author = validated_data.get(
            'author', instance.author)
        instance.title = validated_data.get(
            'title', instance.title)
        instance.text = validated_data.get(
            'text', instance.text)
        instance.created_date = validated_data.get(
            'created_date', instance.created_date)
        instance.published_date = validated_data.get(
            'published_date', instance.published_date)
        instance.save()
        return instance
