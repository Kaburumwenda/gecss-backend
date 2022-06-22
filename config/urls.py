from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finance.urls')),
    path('', include('iam.urls')),
    path('', include('home.urls')),
    path('', include('battery.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
