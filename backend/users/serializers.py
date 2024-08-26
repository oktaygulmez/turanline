import logging
from datetime import timedelta

from django.utils import timezone
from rest_framework import exceptions, serializers
from rest_framework_simplejwt import serializers as jwt_serializers

from mssite import mixins as ms_mixins

from . import mixins, models

logger = logging.getLogger(__name__)


class CustomTokenObtainPairSerializer(
    jwt_serializers.TokenObtainPairSerializer
):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['roles'] = {}
        token['roles']['customer'] = hasattr(user, 'customer')
        token['roles']['provider'] = hasattr(user, 'provider')
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_verified:
            raise exceptions.NotAcceptable(
                detail={
                    'detail': 'User account is not verified.'
                }
            )
        return data


class BaseVerificationSerializer(serializers.Serializer):

    phone_number = serializers.CharField(max_length=16)


class VerificationSerializer(BaseVerificationSerializer):

    purpose = serializers.ChoiceField(
        choices=[
            ('verification', 'Verification'),
            ('reset_password', 'Reset Password')
        ]
    )


class NumberVerificationSerializer(BaseVerificationSerializer):

    verification_code = serializers.CharField(max_length=6)


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User


class BaseNewsSerializer(
    ms_mixins.BaseLocalizationMixin,
    serializers.ModelSerializer
):

    class Meta:
        model = models.News
        translated_fields = [
            'category'
        ]


class UserSerializer(
    mixins.UserMixin,
    BaseUserSerializer
):

    phone_number = serializers.CharField(validators=[])

    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id',
            'email',
            'phone_number',
            'password',
            'first_name',
            'last_name'
        ]


class UserReadSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = [
            'id',
            'email',
            'phone_number',
            'first_name',
            'last_name'
        ]


class ModerationTimeSerializer(serializers.ModelSerializer):

    time_left = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = [
            'time_left'
        ]

    def get_time_left(self, obj):
        now = timezone.now()
        date_joined = obj.date_joined
        elapsed_time = now - date_joined
        remaining_time = timedelta(hours=24) - elapsed_time
        if remaining_time.total_seconds() < 0:
            remaining_time = timedelta(seconds=0)
        return int(remaining_time.total_seconds())


class NewsSerializer(BaseNewsSerializer):

    class Meta(BaseNewsSerializer.Meta):
        fields = '__all__'
        translated_fields = [
            'category'
        ]
