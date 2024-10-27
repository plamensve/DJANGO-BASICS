
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_basics_regular_exam.web.urls')),
    path('posts/', include('django_basics_regular_exam.posts.urls')),
    path('author/', include('django_basics_regular_exam.author.urls')),
]
