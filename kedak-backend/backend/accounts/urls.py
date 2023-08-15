from django.urls import path, include,re_path
from rest_framework import routers
from .views import UserProfileViewSet

router= routers.DefaultRouter()
router.register('userprofiles',UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    
]
