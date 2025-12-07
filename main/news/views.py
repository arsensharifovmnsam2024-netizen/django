from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
import re

from ..models import News


def news_list(request):
    articles = News.objects.all().order_by("-date")
    return render(request, "news.html", {"articles": articles})


def chat_search(request):
    q = (request.GET.get("q") or "").strip()
    results = []

    if q:
        normalized = q.lower()
        tokens = re.findall(r"\w+", normalized, flags=re.U)

        search_q = Q()
        for t in tokens:
            if len(t) < 2:
                continue
            search_q |= Q(title__icontains=t) | Q(content__icontains=t)

        if search_q:
            qs = News.objects.filter(search_q).order_by("-date")[:5]
        else:
            qs = News.objects.none()

        for a in qs:
            snippet = a.content or ""
            if len(snippet) > 150:
                snippet = snippet[:150] + "..."
            results.append(
                {
                    "title": a.title,
                    "snippet": snippet,
                    "link": "/news/",
                }
            )

    return JsonResponse({"results": results})
