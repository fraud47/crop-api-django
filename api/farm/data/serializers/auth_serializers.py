from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data["role"] = user.role if hasattr(user, "role") else None
        data["id"] = user.id if hasattr(user, "id") else None

        return data