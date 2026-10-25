from django.shortcuts import render

from .models import SiteProfile


def home(request):
    profile = SiteProfile.get_profile()
    return render(
        request,
        "links/home.html",
        {
            "profile": profile,
            "links": profile.links.filter(is_active=True),
        },
    )
