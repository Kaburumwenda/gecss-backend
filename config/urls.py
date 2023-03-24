from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     ## API LOGIN
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('', include('finance.urls')),
    path('', include('iam.urls')),
    path('', include('home.urls')),
    path('', include('battery.urls')),
    path('', include('motobikes.urls')),
    path('', include('mpesa.urls')),
    path('', include('HRMS.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
