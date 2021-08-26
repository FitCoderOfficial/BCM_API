from django.db.models import fields
from rest_framework import serializers
from accounts.models import Users

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = Users
        fields = [ "username", "email", "userid", "password", "password2", "phone_number", "sex"]
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        users = Users(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        users.set_password(password)
        users.save()
        return users