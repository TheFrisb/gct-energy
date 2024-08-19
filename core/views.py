from django.shortcuts import render


# Create your views here.
def home_view(request):
    context = {
        "title": "GCT Energy"
    }
    return render(request, "theme/pages/home.html", context=context)


def about_us_view(request):
    context = {
        "title": "About Us"

    }
    return render(request, "theme/pages/about_us.html", context=context)


def contact_us_view(request):
    context = {
        "title": "Contact Us"
    }
    return render(request, "theme/pages/contact_us.html", context=context)


def services_view(request):
    context = {
        "title": "Services"
    }
    return render(request, "theme/pages/services.html", context=context)


def projects_view(request):
    context = {
        "title": "Projects"
    }
    return render(request, "theme/pages/projects.html", context=context)

# def quote_view(request):
#     return render(request, "theme/pages/quote.html")
# def team_view(request):
#     return render(request, "theme/pages/team.html")
#
#
# def features_view(request):
#     return render(request, "theme/pages/features.html")
