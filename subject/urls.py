from django.urls import path
from subject.views import getSubjects, getSubject, addSubject, updateSubject


urlpatterns = [
    path('subjects', getSubjects),
    path('subjects/add', addSubject),
    path('subjects/<id>/update', updateSubject),
    path('subjects/<id>', getSubject)
]
