from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length=8)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length=8)

    @staticmethod
    def validate_email(email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Invalid email.')
        return email

    @staticmethod
    def validate_password1(password):
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError('Password must contain at least one numeral.')
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError('Password must contain at least one letter.')
        return password

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('The two password fields did not match.')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password1'],
        )
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class CurrentPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={'input_type': 'password'})

    def validate_current_password(self, value):
        is_password_valid = self.context['request'].user.check_password(value)
        if is_password_valid:
            return value
        else:
            raise serializers.ValidationError('Invalid password.')


class UserDeleteSerializer(CurrentPasswordSerializer):
    pass
