from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.api.serializers import RegistrationSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        # Check if serializer is valid
        if not serializer.is_valid():
            # Return error response if serializer is not valid
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Save the user instance using the serializer
            user = serializer.save()

            # Create a token for the user using Django Rest Framework Token
            token = Token.objects.create(user=user)

            # Create JWT tokens using Django Rest Framework SimpleJWT
            jwt_token = RefreshToken.for_user(user=user)

        except Exception as e:
            # Handle any unexpected errors during user creation
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare response data
        data = {
            'message': 'User has been created successfully!',
            'token': token.key,  # Include DRF Token key in response
            # 'jwt-token': {
            #     'refresh': str(jwt_token),  # Include JWT refresh token in response
            #     'access': str(jwt_token.access_token),  # Include JWT access token in response
            # }
        }

        # Return success response
        return Response(data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'auth token deleted!'}, status.HTTP_200_OK)
