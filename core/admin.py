from django.contrib import admin

from core.models import Testimonial, TeamMember, CarouselImage, BrandStats


# Register your models here.


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    search_fields = ["title"]
    list_filter = ["created"]
    fieldsets = [
        (None, {"fields": ["title", "description", "image"]}),
    ]
    readonly_fields = ["created", "modified"]


@admin.register(BrandStats)
class BrandStatsAdmin(admin.ModelAdmin):
    list_display = [
        "happy_customers",
        "projects_completed",
        "awards_won",
        "expert_workers",
        "created",
    ]
    list_filter = ["created"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "happy_customers",
                    "projects_completed",
                    "awards_won",
                    "expert_workers",
                ]
            },
        ),
    ]
    readonly_fields = ["created", "modified"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]
    search_fields = ["name"]
    list_filter = ["created"]
    fieldsets = [
        (None, {"fields": ["name", "content", "image"]}),
    ]
    readonly_fields = ["created", "modified"]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ["full_name", "created"]
    search_fields = ["full_name"]
    list_filter = ["created"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "full_name",
                    "profession",
                    "image",
                    "facebook",
                    "twitter",
                    "linkedin",
                ]
            },
        ),
    ]
    readonly_fields = ["created", "modified"]
