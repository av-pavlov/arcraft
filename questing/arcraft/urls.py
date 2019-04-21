from django.urls import path, include

from rest_framework import routers
from .viewsets import *
from .views import *


# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
# router.register(r'questitems', QuestItemViewSet)
router.register(r'locations', LocationViewSet)

# router.register(r'games', GameList.as_view())



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('games/', GameList.as_view(), name='games'),
    path('quests/<int:quest_pk>/items/', QuestItemList.as_view(), name='questitems'),
    path('quests/', QuestList.as_view(), name='quests'),
    path('myquests/', MyQuestList.as_view(), name='myquests'),
    path('users/', UserList.as_view(), name='users'),
]
