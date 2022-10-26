from django.contrib import admin
from app.models import ChatGroup
# Register your models here.

class ChatGroupClass(admin.ModelAdmin):
    list_display=("id","group_name","created_on")

admin.site.register(ChatGroup,ChatGroupClass)
 