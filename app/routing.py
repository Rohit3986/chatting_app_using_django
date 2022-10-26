from django.urls import path
from app.consumers import MyAsyncConsumer
#web_urlpatterns=[path("ws/wc",MyConsumer.as_asgi())]
web_urlpatterns=[path("ws/wc/<str:group_name>",MyAsyncConsumer.as_asgi())]