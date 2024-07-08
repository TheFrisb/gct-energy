from django.urls import path

from core.views import (
    home_view,
    about_us_view,
    contact_us_view,
    team_view,
    features_view,
    services_view,
    projects_view,
    quote_view,
)

app_name = "core"
urlpatterns = [
    path("", home_view, name="home"),
    path("about-us/", about_us_view, name="about_us"),
    path("contact-us/", contact_us_view, name="contact_us"),
    path("team/", team_view, name="team"),
    path("features/", features_view, name="features"),
    path("services/", services_view, name="services"),
    path("projects/", projects_view, name="projects"),
    path("quote/", quote_view, name="quote"),
]
