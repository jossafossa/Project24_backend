from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.FriendCircle)
admin.site.register(models.FriendCircleMembership)
admin.site.register(models.FriendCircleMatcher)

