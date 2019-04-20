from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(QuestItem)
admin.site.register(Quest)
admin.site.register(Game)
admin.site.register(GameItem)
admin.site.register(GameEvent)
