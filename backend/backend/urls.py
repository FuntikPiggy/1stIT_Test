import smart_selects
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('api/', include('api.urls')),
]
