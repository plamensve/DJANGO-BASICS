from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from petstagram_2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_2.common.urls')),
    path('accounts/', include('petstagram_2.accounts.urls')),
    path('pets/', include('petstagram_2.pets.urls')),
    path('photos/', include('petstagram_2.photos.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)