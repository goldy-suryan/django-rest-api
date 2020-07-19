from django.shortcuts import render
from rest_framework.decorators import api_view
from subject.models import SubjectModel
from subject.serializer import SubjectSerializer
from rest_framework.response import Response
from bson import ObjectId
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def getSubjects(request):
    try:
        subjects = SubjectModel.objects.all()
        serial = SubjectSerializer(subjects, many=True)
        return Response(serial.data)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def getSubject(request, id):
    try:
        id = ObjectId(id)
        subjects = SubjectModel.objects.get(pk=id)
        serial = SubjectSerializer(subjects, many=False)
        return Response(serial.data)
    except SubjectModel.DoesNotExist:
        return Response('Subject Does not Exists', status = status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updateSubject(request, id):
    try:
        id = ObjectId(id)
        subject = SubjectModel.objects.get(pk=id)
        subject_serializer = SubjectSerializer(subject, data=request.data)
        if subject_serializer.is_valid():
            subject_serializer.save()
            return Response(subject_serializer.data, status=status.HTTP_200_OK)
        return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except SubjectModel.DoesNotExist:
        return Response('Subject Does not exists', status = status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def addSubject(request):
    try:
        subject_serializer = SubjectSerializer(data=request.data)
        if(subject_serializer.is_valid()):
            subject_serializer.save()
            return Response(subject_serializer.data, status=status.HTTP_200_OK)
        return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def removeSubject(request, id):
    try:
        id = ObjectId(id)
        subject = SubjectModel.objects.get(pk=id)
        subject.delete()
        return Response('Subject deleted successfully', status = 204)
    except SubjectModel.DoesNotExist:
        return Response('Subject Does not exists', status = status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)