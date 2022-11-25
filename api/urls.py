from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("edu/", views.edu, name="edu"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("hobbies/", views.hobbies, name="hobbies"),
    path("contacts/", views.contacts, name="contacts"),
]