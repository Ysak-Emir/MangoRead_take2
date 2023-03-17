from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mango.models import MangoCard, Review
from users.models import User


# class TypeSerializer()

class CardCreateSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()

    class Meta:
        model = MangoCard
        fields = 'title year description type genre'.split()

    def get_type(self, instance):
        return instance.type.type_title

    def get_genre(self, instance):
        return instance.genre.genre_title

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
        return instance.genre.genre_title

    def get_type(self, instance):
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



class ReviewCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    text = serializers.CharField(max_length=200, required=True)
    mango_id = serializers.IntegerField()

    def create(self, validated_data):
        return Review.objects.create(
            user_id=validated_data["user_id"],
            text=validated_data["text"],
            mango_id=validated_data["mango_id"]
        )