from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Ima put em here later'
    }

    return Response(api_urls)




# Create your views here.
# def index(request):
#     context = {
#         "about": About.objects.last(),
#         "edu": Education.objects.all(),
#         "skills": Skill.objects.all(),
#         "projects": Project.objects.all(),
#         "contacts": Contact.objects.all(),
#         "hobbies": Hobby.objects.all()
#     }

#     return render(request, "api/index.html", context)