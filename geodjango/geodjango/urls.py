from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from world.views import WorldBorderViewSet


router = routers.DefaultRouter()
router.register('border', WorldBorderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('world/', include(router.urls)),
]
