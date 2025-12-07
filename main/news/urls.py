from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("chat-search/", views.chat_search, name="chat_search"),
]
