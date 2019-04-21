from .models import *
from .serializers import GameSerializer, QuestSerializer, QuestItemSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import GameSerializer
from django.contrib.auth.models import User
from django.db.models import Q

from datetime import datetime


class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        return self.queryset.filter(users__in=(self.request.user,))

    def post(self, request, format=None):
        request.data['start_time'] = datetime.now()
        serializer = GameSerializer(data=request.data, context={'request': request}, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestList(generics.ListAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    def get_queryset(self):
        current_user = User.objects.get(pk=2) #self.request.user
        return self.queryset.filter(~Q(author=current_user))


class MyQuestList(generics.ListCreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    def get_queryset(self):
        current_user = User.objects.get(pk=2)  # self.request.user
        return self.queryset.filter(author=current_user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestItemList(generics.ListCreateAPIView):
    queryset = QuestItem.objects.all()
    serializer_class = QuestItemSerializer

    def get_queryset(self):
        quest = Quest.objects.get(pk=self.kwargs['quest_pk'])
        return self.queryset.filter(quest=quest)