from django.urls import path
from blog.views import getBlogs, getBlog, updateBlog, addBlog

urlpatterns = [
    path('blogs', getBlogs),
    path('blogs/add', addBlog),
    path('blogs/<id>', getBlog),
    path('blogs/<id>/update', updateBlog),
]
