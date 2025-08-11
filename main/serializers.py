from rest_framework import serializers

from main.models import Article, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "surname",
            "nick",
            "email",
            "bio",
            "password",
            "created_at",
        ]
