from django.contrib import admin
from django.urls import path, include
from api_ss.urls import router

urlpatterns = [
    path('api/v1/', include('api_ss.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
