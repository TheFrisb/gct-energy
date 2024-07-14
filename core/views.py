from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, "theme/pages/home.html")


def about_us_view(request):
    return render(request, "theme/pages/about_us.html")


def contact_us_view(request):
    return render(request, "theme/pages/contact_us.html")


def services_view(request):
    return render(request, "theme/pages/services.html")


def projects_view(request):
    return render(request, "theme/pages/projects.html")

# def quote_view(request):
#     return render(request, "theme/pages/quote.html")
# def team_view(request):
#     return render(request, "theme/pages/team.html")
#
#
# def features_view(request):
#     return render(request, "theme/pages/features.html")
