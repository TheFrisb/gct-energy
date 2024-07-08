from core.models import Testimonial, TeamMember, CarouselImage, BrandStats


def fetch_common_data(request):
    """
    This function will fetch the common data for all the views
    :param request:
    :return:
    """
    return {
        "testimonials": Testimonial.objects.all(),
        "team_members": TeamMember.objects.all(),
        "carousel_images": CarouselImage.objects.all(),
        "brand_stats": BrandStats.objects.first(),
    }
