from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mango.models import MangoCard, Review
from users.models import User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoCard
        fields = ["profile_picture", "title", "year", "description", "genre", "type"]


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoCard
        fields = "id profile_picture title year description".split()


class CardDetailSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = MangoCard
        fields = "id profile_picture title year description time_create genre type".split()

    @staticmethod
    def get_type(instance):
        return instance.type.type_title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username nickname".split()


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Review
        fields = 'id user text time_create'.split()
        read_only_fields = ['time_create']


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
