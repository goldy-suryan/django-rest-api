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
    subjects = SubjectModel.objects.all()
    serial = SubjectSerializer(subjects, many=True)
    return Response(serial.data)

@api_view(['GET'])
def getSubject(request, id):
    id = ObjectId(id)
    subjects = SubjectModel.objects.get(pk=id)
    serial = SubjectSerializer(subjects, many=False)
    return Response(serial.data)


@api_view(['PUT'])
def updateSubject(request, id):
    id = ObjectId(id)
    subject = SubjectModel.objects.get(pk=id)
    subject_serializer = SubjectSerializer(subject, data=request.data)
    if subject_serializer.is_valid():
        subject_serializer.save()
        return Response(subject_serializer.data, status=status.HTTP_200_OK)
    return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addSubject(request):
    subject_serializer = SubjectSerializer(data=request.data)
    if(subject_serializer.is_valid()):
        subject_serializer.save()
        return Response(subject_serializer.data, status=status.HTTP_200_OK)
    return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)