from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import ParseError
from .serializers import *

from rest_framework import permissions


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class QuestItemViewSet(viewsets.ModelViewSet):
    queryset = QuestItem.objects.all()
    serializer_class = QuestItemSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = (permissions.IsAuthenticated,)

# class ItemViewSet(viewsets.BaseViewSet, viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#     @detail_route(methods=['post'])
#     def upload_docs(request):
#         try:
#             file = request.data['file']
#         except KeyError:
#             raise ParseError('Request has no resource file attached')
#         product = Product.objects.create(image=file, ....)