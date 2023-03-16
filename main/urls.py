from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('users.urls')),
    path('api/v1/mango/', include('mango.urls')),
]

urlpatterns += static(settings.base.STATIC_URL, document_root=settings.base.STATIC_ROOT)
urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)