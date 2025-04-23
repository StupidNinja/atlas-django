from rest_framework import serializers
from .models import Todo, Category, Tag, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'todo', 'user', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']
        
class TodoSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'priority', 'created_at', 'updated_at', 'category', 'tags', 'comments']
     
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        todo = super().create(validated_data)
        todo.tags.set(tags)
        return todo

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        todo = super().update(instance, validated_data)
        if tags is not None:
            todo.tags.set(tags)
        return todo



# Using Serializer (manual implementation)
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance