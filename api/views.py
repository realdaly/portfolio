from django.http import JsonResponse
from .models import *



def about(request):
    data = list(About.objects.values())
    return JsonResponse(data, safe=False)


def edu(request):
    data = list(Education.objects.values())
    return JsonResponse(data, safe=False)


def skills(request):
    data = list(Skill.objects.values())
    return JsonResponse(data, safe=False)


def projects(request):
    data = list(Project.objects.values())
    return JsonResponse(data, safe=False)


def hobbies(request):
    data = list(Hobby.objects.values())
    return JsonResponse(data, safe=False)


def contacts(request):
    data = list(Contact.objects.values())
    return JsonResponse(data, safe=False)