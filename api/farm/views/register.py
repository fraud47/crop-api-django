from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from ..data.response.api_response import ApiResponse
from ..data.serializers.user_serializers import UserSerializer
from ..models import User
from rest_framework import permissions


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated access

    @swagger_auto_schema(
        operation_description="Register a new user",
        request_body=UserSerializer,
        responses={
            201: openapi.Response(
                description="User successfully registered",
                examples={
                    "application/json": {
                        "successful": True,
                        "narration": "User registered successfully",
                        "status": 201,
                        "body": {
                            "id": 1,
                            "username": "newuser",
                            "email": "newuser@example.com"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "successful": False,
                        "narration": "ERROR",
                        "status": 400,
                        "body": {
                            "username": ["This field is required."]
                        }
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return ApiResponse(
            body=response.data,
            status_code=status.HTTP_201_CREATED,
            narration="User registered successfully"
        )