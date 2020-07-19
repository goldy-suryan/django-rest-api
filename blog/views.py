from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from blog.serializer import BlogSerializer
from blog.models import BlogModel
from rest_framework.response import Response
from bson import ObjectId

# Create your views here.
@api_view(['GET'])
def getBlogs(request):
    try:
        blog_post = BlogModel.objects.all()
        serializer = BlogSerializer(blog_post, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getBlog(request, id):
    try:
        id = ObjectId(id)
        blog_post = BlogModel.objects.get(pk=id)
        serial = BlogSerializer(blog_post, many=False)
        return Response(serial.data, status=status.HTTP_200_OK)
    except BlogModel.DoesNotExist:
        return Response('Blog Does not exists', status = status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updateBlog(request, id):
    try:
        id = ObjectId(id)
        blog_post = BlogModel.objects.get(pk=id)
        blog_serializer = BlogSerializer(blog_post, data=request.data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return Response(blog_serializer.data, status=status.HTTP_200_OK)
        return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except BlogModel.DoesNotExist:
        return Response('Blog Does not exists', status = status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def addBlog(request):
    try:
        blog_serializer = BlogSerializer(data=request.data)
        if(blog_serializer.is_valid()):
            blog_serializer.save()
            return Response(blog_serializer.data, status=status.HTTP_200_OK)
        return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)