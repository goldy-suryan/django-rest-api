from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from bson import ObjectId

# Create your views here.
@api_view(['GET'])
def getPaths(request):
    return Response({
        'blogs': '/api/blogs',
        'single blog': '/api/blogs/<id>',
        'update blog': '/api/blogs/<id>/update',
        'add blog': '/api/blogs/add',
        'subjects': '/api/subjects',
        'add subject': '/api/subjects/add',
        'single subject': '/api/subjects/<id>',
        'udpate subject': '/api/subjects/<id>/update'
    })