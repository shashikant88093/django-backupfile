from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import ModelSerializer
from .models import User, Table
from rest_framework import serializers
from django.contrib.auth import password_validation

class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'change_password'
            # 'first_name',
            # 'last_name',
            # 'phone'
        )


class TableSerializer(ModelSerializer):
    class Meta:
        # user: UserCreateSerializers(read_only=True)
        model = Table
        fields = (
            # 'username',
            'Run_ID',
            'Date_time',
            'Run_status',
            'count',
            'path',
            'created_at'
        )

    def get_user(self, obj):
        return str(obj.Run_ID)


class TableDetailSerializer(ModelSerializer):
    class Meta:
        # user: UserCreateSerializers(read_only=True)
        model = Table
        fields = (
            # 'username',
            # 'Run_ID',
            'Date_time',
            # 'Run_status',
            # 'count',
            'path',
            'created_at'
        )



class ChangePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        old_password = serializers.CharField(max_length=128, write_only=True, required=True)
        new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
        new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user