from django.urls import path
from .views import *

urlpatterns = [
    path("webhook/", telegram_webhook),
    path("messages/", messages_list),
    path("test-send/", test_send),
]
