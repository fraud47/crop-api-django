from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.auth import CustomTokenObtainPairView, CustomTokenRefreshView
from .views.crop import CropViewSet
from .views.farm import FarmCreateView
from .views.farm_type import FarmTypeViewSet
from .views.register import UserCreateView

router = DefaultRouter()
router.register(r'crop', CropViewSet)
router.register(r'farmtype', FarmTypeViewSet)

urlpatterns = [
    path('farmers/',FarmCreateView.as_view(),name='farmers-list-create'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    ] + router.urls
