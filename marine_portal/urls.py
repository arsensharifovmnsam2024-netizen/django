from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from two_factor.urls import urlpatterns as tf_urls


def index(request):
    return render(request, "index.html")


urlpatterns = [
    path("", index, name="home"),
    path("", include(tf_urls)),
    path("admin/", admin.site.urls),
    path("news/", include("main.news.urls")),
]
