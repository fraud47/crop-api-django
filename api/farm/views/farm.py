# Clerk submits farmer data
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.response import Response

from ..data.response.api_response import ApiResponse
from ..models import Farmer
from ..data.serializers import FarmSerializer
from ..utils.permissions import IsAdmin


class FarmCreateView(generics.CreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


    def get_permissions(self):
        if self.request.method == 'POST':  # Allow only authenticated users to create
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsAdmin()]


    @swagger_auto_schema(
        operation_description="create farm ",  # Description of what the GET endpoint does
        responses={200: FarmSerializer()}  # Expected response: 200 status with a list of MyModel instances serialized
    )
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @swagger_auto_schema(
        operation_description="Retrieve all Farms instances",  # Description of what the GET endpoint does
        responses={200: FarmSerializer(many=True)}  # Expected response: 200 status with a list of MyModel instances serialized
    )
    def get(self, request):
        models = Farmer.objects.all()  # Fetch all MyModel instances from the database
        serializer = FarmSerializer(models, many=True)  # Serialize the instances
        return ApiResponse(serializer.data)  # Return the serialized data in the response


