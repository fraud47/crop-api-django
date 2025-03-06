from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..data.response.api_response import ApiResponse
from ..data.serializers.auth_serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    @swagger_auto_schema(
        operation_description="Login and obtain JWT token",
        responses={200: openapi.Response("JWT Token returned")},
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return ApiResponse(body=response.data, status_code=status.HTTP_200_OK)

class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_description="Refresh JWT token",
        responses={200: openapi.Response("New JWT Token returned")},
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return ApiResponse(body=response.data, status_code=status.HTTP_200_OK)
