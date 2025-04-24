from rest_framework import serializers
from .models import Todo, Category, Tag, Comment, TaskStatus

# Using ModelSerializer
class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TodoSerializer(serializers.ModelSerializer):
    status = TaskStatusSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    # Разрешаем принимать идентификаторы при записи:
    status_id = serializers.PrimaryKeyRelatedField(source='status', queryset=TaskStatus.objects.all(), write_only=True)
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'description', 'completed', 'priority', 'created_at', 'updated_at',
                  'status', 'category', 'status_id', 'category_id']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'todo', 'user', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']

# Using Serializer (manual implementation)
class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance