
from django.contrib import admin
from django.urls import path, include

from world_of_speed.car.views import catalogue
from world_of_speed.web.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('world_of_speed.web.urls')),
    path('car/', include('world_of_speed.car.urls')),
    path('profile/', include('world_of_speed.profilee.urls'))
]
