from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="apiOverview"),
    # path("about/", views.about, name="about"),
    # path("edu/", views.edu, name="edu"),
    # path("skills/", views.skills, name="skills"),
    # path("projects/", views.projects, name="projects"),
    # path("contacts/", views.contacts, name="contacts"),
    # path("hobbies/", views.hobbies, name="hobbies")
]