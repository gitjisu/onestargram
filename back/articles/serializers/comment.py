from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Comment
from .reply import ReplySerializer

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_img')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article', 'created_at')
        read_only_fields = ('article', )