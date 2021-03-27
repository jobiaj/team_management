from rest_framework import serializers
from team.models import Teammembers


class TeamSerializer(serializers.ModelSerializer):

    """
    Serializer class for Teammembers Model
    """
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    phone = serializers.CharField(source="phone_number")
    emailId = serializers.CharField(source="email")

    class Meta:
        model = Teammembers
        fields = ('id', 'firstName', 'lastName', 'phone', 'emailId', 'role')