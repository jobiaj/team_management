from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics, serializers

from rest_framework.response import Response
from team.models import Teammembers
from team.serializers import TeamSerializer



# @api_view(['GET'])
# def team_members_list(request):
#     if request.method == 'GET':
#         team_members = Teammembers.objects.all()
#         serializer = TeamSerializer(team_members, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def get_team_member(request, pk):
#     try:
#         team_member = Teammembers.objects.get(pk=pk)
#     except Teammembers.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = TeamSerializer(team_member)
#         return Response(serializer.data)


class TeamDataList(generics.ListCreateAPIView):
    """
    Teammembers List View class to list all the active Teammembers objects
    Also, responsible to create the new resource
    """
    serializer_class = TeamSerializer

    def get_queryset(self):
        """
        This view should return a list of all the Teammembers
        for the user.
        """
        return Teammembers.objects.all()


class TeamMemberDetails(generics.RetrieveUpdateDestroyAPIView):
    """
     TeamMember Details View class
     This class renders the detailed view for given TeamMember object
     Also, responsible for updating and archiving the TeamMember
    """
    serializer_class = TeamSerializer

    def get_queryset(self):
        """
        This view should return a list of all the XMLData
        having is_archived as False
        """
        return Teammembers.objects.all()