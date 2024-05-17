from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.serializers import RegistrationSerializer


class LoginView:
    pass


class RegisterView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        # Check if serializer is valid
        if not serializer.is_valid():
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Get the user instance
            user = serializer.save()
            # Create a token for the user
            token = Token.objects.create(user=user)
        except Exception as e:
            # Handle any unexpected errors during user creation
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'message': 'User has been created successfully!',
            'user': serializer.data,
            'token': token.key,
        }

        # Return success response
        return Response(data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'auth token deleted!'}, status.HTTP_200_OK)
