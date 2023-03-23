from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mango.models import MangoCard, Review
from users.models import User


# class TypeSerializer()

# class CardSerializer(serializers.Serializer):
#     profile_picture = serializers.ImageField(default="null")
#     title = serializers.CharField(max_length=100)
#     year = serializers.IntegerField(max_value=3000)
#     description = serializers.CharField(max_length=2000)
#     genre_id = serializers.IntegerField()
#     type_id = serializers.IntegerField()


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoCard
        fields = ["profile_picture", "title", "year", "description", "genre", "type"]



class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoCard
        fields = "id profile_picture title year description".split()


class CardDetailSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = MangoCard
        fields = "id profile_picture title year description time_create genre type".split()

    def get_genre(self, instance):
        return instance.genre.genre

    def get_type(self, instance):
        return instance.type.type


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


class ReviewCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    text = serializers.CharField(max_length=200, required=True)
    mango = serializers.IntegerField()

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
