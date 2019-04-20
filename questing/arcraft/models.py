from django.db.models import *
from django.contrib.auth.models import User


class Item(Model):
    CATEGORIES= (
        ('IMG', 'Image'),
        ('TXT', 'Text Note'),
        ('TRO', 'Trophy'),
        ('OTH', 'Other')
    )
    name = CharField(max_length=30)
    category = CharField('item category', max_length=3, choices=CATEGORIES)
    uploader = ForeignKey(User, on_delete=CASCADE, verbose_name='uploaded by')
    model = FileField(upload_to='models/')
    thumb = ImageField(upload_to='models/', null=True, blank=True)
    __str__ = lambda self: self.name


class Location(Model):
    lat = FloatField('latitude')
    lon = FloatField('longitude')


class QuestItem(Model):
    item = ForeignKey(Item, on_delete=CASCADE)
    required_items = ManyToManyField("self", blank=True)
    possible_locations = ManyToManyField(Location)
    text = TextField()
    descr = TextField("description for inventory")
    image = ImageField(null=True, blank=True)


class Quest(Model):
    """A recipe for a quest listing all items"""
    name = CharField(max_length=60)
    cover = ImageField("Cover image", null=True, blank=True)
    quest_items = ManyToManyField(QuestItem, blank=True)
    author = ForeignKey(User, on_delete=CASCADE, related_name='authored_quests')
    creation_time = DateTimeField(auto_now_add=True, blank=True)
    played = IntegerField('number of times played', default=0)
    rating = FloatField(default=0)

    def __str__(self):
        return "{} (by {})".format(self.name, self.author.username)


class Game(Model):
    """An instantiated game in progress"""
    users = ManyToManyField(User, related_name='games')
    quest = ForeignKey(Quest, on_delete=CASCADE)
    start_time = DateTimeField('date started')

    def __str__(self):
        return "{} (started on {})".format(self.quest.name, self.start_time)


class GameItem(Model):
    game = ForeignKey(Game, on_delete=CASCADE)
    quest_item = ForeignKey(QuestItem, on_delete=CASCADE)
    lat = FloatField('latitude')
    lon = FloatField('longitude')


class GameEvent(Model):
    game_item = ForeignKey(GameItem, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    discovery_time = DateTimeField('discovered on', null=True, db_index=True)


class QuestRating(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    quest = ForeignKey(Quest, on_delete=CASCADE)
    rating = IntegerField()
