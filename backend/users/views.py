from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import CurrentUserOrAdmin
from users.serializers import UserCreateSerializer, UserDeleteSerializer, UserSerializer


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.all()
        if settings.HIDE_USERS and not user.is_staff:
            queryset = queryset.filter(pk=user.pk)

        return queryset

    def get_instance(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'destroy' or (self.action == 'me' and self.request and self.request.method == 'DELETE'):
            return UserDeleteSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        elif self.action == 'list':
            self.permission_classes = [CurrentUserOrAdmin]
        elif self.action == 'destroy' or (self.action == 'me' and self.request and self.request.method == 'DELETE'):
            self.permission_classes = [CurrentUserOrAdmin]

        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(['get', 'put', 'patch', 'delete'], detail=False)
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_instance
        match self.request.method:
            case 'GET':
                return self.retrieve(request, *args, **kwargs)
            case 'PUT':
                return self.update(request, *args, **kwargs)
            case 'PATCH':
                return self.partial_update(request, *args, **kwargs)
            case 'DELETE':
                return self.destroy(request, *args, **kwargs)
