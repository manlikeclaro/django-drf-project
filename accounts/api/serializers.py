from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        # Check if the two passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': "The two password fields didn't match."})

        # Validate the password using Django's built-in validators
        try:
            validate_password(data['password'])
        except serializers.ValidationError as error:
            # raise serializers.ValidationError({"password": exc.detail})
            raise serializers.ValidationError({"password": error})

        # Check if the email is already in use
        if User.objects.filter(email__iexact=data['email']).exists():
            raise serializers.ValidationError({'email': "A user with that email already exists."})

        return data

    def create(self, validated_data):
        # Create the user without the password2 field
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
