from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()


class Register_Serializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class Login_Serializer (serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = User.objects.filter(username=username)
        if user.exists():
            user = authenticate(request=self.context.get("request"), username=username, password=password)
        else:
            msg = {
                'detail': 'Unable to log in with provided credentials.'}
            raise serializers.ValidationError(msg)
        attrs["user"] = user
        return attrs
