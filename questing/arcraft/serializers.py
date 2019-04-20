from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'date_joined',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        exclude = ('quest_items', )


class QuestItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestItem
        fields = ('item', 'required_items', 'possible_locations', 'text', 'descr', 'image')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('quest', 'users')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'lon')

