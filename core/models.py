from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CarouselImage(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Image Title")
    description = models.TextField(verbose_name="Image Description")
    image = models.ImageField(upload_to="carousel/", verbose_name="Carousel Image")

    def __str__(self):
        return self.title


class BrandStats(TimeStampedModel):
    happy_customers = models.IntegerField(verbose_name="Happy Customers")
    projects_completed = models.IntegerField(verbose_name="Projects Completed")
    awards_won = models.IntegerField(verbose_name="Awards Won")
    expert_workers = models.IntegerField(verbose_name="Expert Workers")

    def __str__(self):
        return "Brand Stats"


class Testimonial(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    content = models.TextField(verbose_name="Testimonial content")
    profession = models.CharField(max_length=255, verbose_name="Profession")
    image = models.ImageField(upload_to="testimonials/", verbose_name="Avatar Image")

    def __str__(self):
        return self.name


class TeamMember(TimeStampedModel):
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    profession = models.CharField(max_length=255, verbose_name="Profession")
    image = models.ImageField(upload_to="team/", verbose_name="Avatar Image")
    facebook = models.URLField(verbose_name="Facebook URL", blank=True, null=True)
    twitter = models.URLField(verbose_name="Twitter URL", blank=True, null=True)
    linkedin = models.URLField(verbose_name="LinkedIn URL", blank=True, null=True)

    def __str__(self):
        return self.full_name
