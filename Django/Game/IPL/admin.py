from django.contrib import admin

from .models import Player, Team, Post

# Register your models here.


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Post)