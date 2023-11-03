from django.db import models
from django.contrib import admin 
class Football_Player(models.Model):
    Player_id=models .CharField(max_length=15)
    Player_name=models.CharField(max_length=30)
    Event=models.CharField(max_length=50)
    Category=models.CharField(max_length=20)
    Age=models.IntegerField()
class Football_PlayerAdmin(admin.ModelAdmin):
    list_display=["Player_id","Player_name","Event","Category","Age"]    

